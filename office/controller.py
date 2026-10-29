"""File-based office controller. No model calls, credentials, paid APIs or messages."""
import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path, PurePosixPath
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
STAGES = [
    ('research', 'Tìm đề tài art/design có nguồn', 'research.md', 9),
    ('plan', 'Lập kế hoạch kênh và thử nghiệm nội dung', 'plan.md', 10),
    ('script', 'Viết kịch bản, storyboard và caption SaLu', 'script.md', 11),
    ('video', 'Dựng video, âm thanh và phụ đề', 'video.mp4', 14),
    ('review', 'Kiểm tra nội dung, nguồn, quyền sử dụng và chất lượng', 'review.json', 16),
    ('publish', 'Đăng thành phẩm đã đạt điều kiện', 'published.json', 18),
    ('measure', 'Ghi hiệu quả và đề xuất cho vòng sau', 'metrics.json', 18),
]


def load(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding='utf-8'))


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def timestamp(value):
    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        raise ValueError('Thiếu múi giờ')
    return dt


def artifact_path(root, task, relative):
    # Every deliverable belongs to this exact task. Never read config/secrets paths.
    p = PurePosixPath(relative)
    prefix = PurePosixPath('office/artifacts') / task['id']
    if p.is_absolute() or '..' in p.parts or not p.is_relative_to(prefix):
        raise ValueError('Đầu ra phải nằm trong thư mục artifact riêng của nhiệm vụ')
    candidate = root / p
    if candidate.is_symlink() or any(parent.is_symlink() for parent in candidate.parents if parent != root):
        raise ValueError('Không nhận đầu ra qua symlink')
    resolved = candidate.resolve()
    if not resolved.is_relative_to((root / prefix).resolve()):
        raise ValueError('Đường dẫn đầu ra không hợp lệ')
    if not resolved.is_file() or resolved.stat().st_size == 0:
        raise ValueError('Chưa có tệp đầu ra hoặc tệp rỗng')
    return resolved


def receipt(root, task, now):
    p = root / 'office/submissions' / (task['id'] + '.json')
    if not p.exists():
        return None
    try:
        r = load(p)
        if r.get('task_id') != task['id'] or r.get('worker') != task['worker']:
            raise ValueError('Sai mã nhiệm vụ hoặc worker')
        at = timestamp(r['submitted_at'])
        if at > now or at < timestamp(task['created_at']):
            raise ValueError('Thời điểm bàn giao không hợp lệ')
        if r.get('status') == 'blocked':
            return {'status': 'blocked', 'reason': str(r.get('reason', 'Worker báo đang bị chặn'))[:400]}
        if r.get('status') != 'completed':
            raise ValueError('Trạng thái bàn giao không hợp lệ')
        paths = r.get('artifacts', [])
        if not isinstance(paths, list) or not paths:
            raise ValueError('Thiếu tệp đầu ra')
        files = [artifact_path(root, task, x) for x in paths]
        expected = next(s[2] for s in STAGES if s[0] == task['stage'])
        expected_files = [f for f in files if f.name == expected]
        if not expected_files:
            raise ValueError('Thiếu đầu ra bắt buộc: ' + expected)
        if task['stage'] == 'research' and not r.get('source_urls'):
            raise ValueError('Nghiên cứu cần liên kết nguồn')
        if task['stage'] == 'review':
            review = load(expected_files[0])
            if not all(review.get(k) is True for k in ['content_pass', 'sources_checked', 'rights_checked', 'platform_checked']):
                raise ValueError('Kiểm duyệt chưa đạt đủ tiêu chí')
        if task['stage'] == 'publish':
            pub = load(expected_files[0])
            if not str(pub.get('url', '')).startswith('https://'):
                raise ValueError('Thiếu link bài đã đăng')
        return {'status': 'completed', 'artifacts': paths, 'submitted_at': r['submitted_at'], 'note': 'Có tệp bàn giao; nội dung do worker chịu trách nhiệm kiểm tra.'}
    except (ValueError, KeyError, TypeError, OSError) as exc:
        return {'status': 'invalid', 'reason': str(exc)[:400]}


def run(root=ROOT, now=None):
    cfg = load(root / 'office/config.json')
    now = now or datetime.now(ZoneInfo(cfg['timezone']))
    now = now.astimezone(ZoneInfo(cfg['timezone']))
    board_path = root / 'office/board.json'
    board = load(board_path, {'version': 1, 'tasks': []})
    day = now.date().isoformat()
    campaign = load(root / 'office/campaign.json')
    cycle = campaign['id']
    if not any(t['cycle'] == cycle for t in board['tasks']):
        prior = None
        for stage, title, filename, hour in STAGES:
            task_id = cycle + '-' + stage
            due = now.replace(hour=hour, minute=0, second=0, microsecond=0)
            if stage == 'measure':
                due += timedelta(days=1)
            board['tasks'].append({'id': task_id, 'cycle': cycle, 'stage': stage, 'title': title,
                'worker': cfg['stage_workers'].get(stage), 'created_at': now.isoformat(),
                'due_at': due.isoformat(), 'depends_on': [prior] if prior else [],
                'expected_output': 'office/artifacts/' + task_id + '/' + filename})
            prior = task_id
    by_id = {t['id']: t for t in board['tasks']}
    decisions = []
    preparation = []
    for key, title in [('platforms', 'Chọn nền tảng và tài khoản kênh'), ('kpi_scope', '1.000 follow cho từng kênh hay tổng các kênh?'), ('deadline', 'Chọn thời hạn mục tiêu'), ('baseline_followers', 'Xác nhận số follow ban đầu'), ('budget_vnd', 'Xác nhận mức chi: 0 đồng hoặc ngân sách cho phép')]:
        if campaign.get(key) is None or campaign.get(key) == []:
            preparation.append({'id': 'campaign-' + key, 'title': title, 'reason': 'Leader cần nghiên cứu và đề xuất phương án, ghi rõ giả định trước khi xin quyết định.', 'file': 'office/campaign.json'})
    for t in board['tasks']:
        t['worker'] = cfg['stage_workers'].get(t['stage'])
        # Rebuild state from evidence every run; never trust an old green status.
        t.update(status='waiting', reason='', artifacts=[])
        worker = t['worker']
        if worker is None or worker not in cfg['workers']:
            t.update(status='blocked', reason='Chưa phân công worker cho bước này')
        elif any(by_id[d]['status'] != 'completed' for d in t['depends_on']):
            t.update(status='waiting', reason='Chờ đầu ra hợp lệ từ bước trước')
        elif t['stage'] == 'publish' and not (cfg['publishing_policy']['enabled'] and cfg['publishing_policy']['charter_approved'] and cfg['publishing_policy']['channel']):
            t.update(status='blocked', reason='Chưa cấu hình kênh và nguyên tắc xuất bản')
        else:
            evidence = receipt(root, t, now)
            if evidence:
                t.update(evidence)
            else:
                t.update(status='ready', reason='Có nhiệm vụ; chưa có báo cáo nhận việc hoặc hoàn thành')
                if not cfg['workers'][worker]['external_schedule_confirmed']:
                    t['reason'] = 'Sẵn sàng bàn giao; chưa xác nhận lịch chạy trong ứng dụng AI'
        t['overdue'] = now > timestamp(t['due_at']) and t['status'] != 'completed'
    for stage in ['video', 'review', 'publish']:
        if not cfg['stage_workers'].get(stage):
            preparation.append({'id': 'assign-' + stage, 'title': 'Chọn worker: ' + dict((x[0], x[1]) for x in STAGES)[stage],
                'reason': 'Chưa có worker được xác nhận thực hiện bước này.', 'file': 'office/config.json'})
    preparation.append({'id': 'confirm-worker-schedules', 'title': 'Xác nhận lịch của từng ứng dụng AI',
        'reason': 'GitHub chỉ tạo nhiệm vụ và thu báo cáo; không tự khởi chạy phiên Claude/Grok/ChatGPT.', 'file': 'office/README.md'})
    plan = next((t for t in board['tasks'] if t['cycle'] == cycle and t['stage'] == 'plan'), None)
    if plan and plan['status'] == 'completed':
        decisions.append({'id': 'review-plan', 'title': 'Xem kế hoạch kênh leader đã bàn giao', 'reason': 'Đã có tệp kế hoạch; cần quyết định các phương án/nền tảng được đề xuất.', 'file': plan['expected_output']})
    board.update(preparation=preparation, campaign=campaign, updated_at=now.isoformat(), schedule_vn=cfg['schedule_vn'], workers=cfg['workers'], decisions=decisions,
        mode='Bộ điều phối theo quy tắc; chưa phải phiên AI leader tự suy luận',
        spending='Không gọi API AI, không mua dịch vụ; chưa thu thập token thực tế')
    save(board_path, board)
    for worker in cfg['workers']:
        assigned = [t for t in board['tasks'] if t['worker'] == worker and t['status'] != 'completed']
        lines = [f'# Nhiệm vụ cho {worker}', '', f'Cập nhật: {now.isoformat()}', '', 'Brief: ' + campaign['brief'], 'Phạm vi: ' + campaign['scope'], '',
            'Đọc office/README.md trước khi làm. Chỉ nhận việc có trạng thái ready. Không làm lại việc đã nộp.']
        for t in assigned:
            lines += ['', f"## {t['id']} — {t['status']}", t['title'], 'Hạn: ' + t['due_at'],
                'Chờ: ' + ', '.join(t['depends_on']), 'Đầu ra: ' + t['expected_output'], 'Ghi chú: ' + t['reason']]
        (root / 'office/work-orders').mkdir(parents=True, exist_ok=True)
        (root / 'office/work-orders' / (worker + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    today_tasks = [t for t in board['tasks'] if t['cycle'] == cycle]
    lines = ['# Báo cáo điều phối — ' + day, '', 'Bản tổng hợp theo dữ liệu bàn giao, không gọi mô hình AI.', '']
    for t in today_tasks:
        lines.append(f"- {t['title']} | {t['worker'] or 'chưa phân công'} | {t['status']}: {t['reason']}")
    lines += ['', '## Cần quyết định'] + ['- ' + d['title'] for d in decisions]
    lines += ['', '## Leader cần chuẩn bị'] + ['- ' + d['title'] for d in preparation]
    lines += ['', 'Không có số liệu token/hóa đơn được kết nối. Không gửi thông báo ra ngoài.']
    out = root / 'office/reports' / (day + '.md')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return board


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', help='Ngày chạy thử YYYY-MM-DD; dùng 08:00 giờ Việt Nam')
    args = parser.parse_args()
    now = datetime.fromisoformat(args.date + 'T08:00:00+07:00') if args.date else None
    result = run(now=now)
    print('Office board updated:', len(result['tasks']), 'tasks; no external messages or AI API calls')
