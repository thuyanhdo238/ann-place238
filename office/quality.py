"""Validate evidence records, not factual truth or legal certainty."""
import hashlib
from datetime import datetime
from urllib.parse import urlparse


def checked_at(value, now):
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if dt.tzinfo is None or dt > now:
            raise ValueError()
    except (ValueError, TypeError, AttributeError):
        raise ValueError('Thời điểm kiểm tra thiếu/sai hoặc ở tương lai')


def public_url(value):
    p = urlparse(str(value))
    return p.scheme == 'https' and bool(p.hostname) and p.username is None and p.password is None


def validate_sources(data, now):
    if not isinstance(data, dict):
        raise ValueError('Hồ sơ nguồn phải là object')
    sources = data.get('sources')
    claims = data.get('claims')
    if not isinstance(sources, list) or not sources or not isinstance(claims, list) or not claims:
        raise ValueError('Thiếu danh sách nguồn/dữ kiện đã kiểm tra')
    ids = set()
    for source in sources:
        if not isinstance(source, dict) or not all(source.get(k) for k in ['id','url','publisher','title','evidence_locator']):
            raise ValueError('Nguồn thiếu thông tin hoặc vị trí bằng chứng')
        if source['id'] in ids or not public_url(source['url']):
            raise ValueError('Mã nguồn trùng hoặc URL không hợp lệ')
        if source.get('verification') != 'checked' or source.get('kind') not in ['primary','secondary']:
            raise ValueError('Nguồn chưa được báo đã mở kiểm tra')
        checked_at(source.get('retrieved_at'), now)
        ids.add(source['id'])
    for claim in claims:
        if not isinstance(claim, dict) or not all(claim.get(k) for k in ['id','statement','verified_by']):
            raise ValueError('Dữ kiện thiếu người xác minh hoặc nội dung')
        refs = claim.get('source_ids')
        if not isinstance(refs, list) or not refs or any(x not in ids for x in refs):
            raise ValueError('Dữ kiện chưa liên kết nguồn có trong hồ sơ')
        if claim.get('support') not in ['direct','inference']:
            raise ValueError('Cần tách dữ kiện trực tiếp và suy luận')
        checked_at(claim.get('checked_at'), now)


def validate_review(data, worker, creator_workers, video_path, video_relative, now):
    if worker in creator_workers or data.get('reviewer') != worker:
        raise ValueError('Reviewer phải khác worker sáng tạo/sản xuất và đúng người nhận việc')
    checked_at(data.get('checked_at'), now)
    if data.get('decision') != 'pass' or data.get('risk') != 'green' or data.get('issues'):
        raise ValueError('Hồ sơ kiểm duyệt còn vấn đề hoặc chưa đạt')
    signature = hashlib.sha256(video_path.read_bytes()).hexdigest()
    records = data.get('reviewed_artifacts', [])
    if not any(isinstance(x, dict) and x.get('path') == video_relative and x.get('sha256') == signature for x in records):
        raise ValueError('Bản video hiện tại khác/thiếu hash của bản đã duyệt')
    assets = data.get('assets')
    if not isinstance(assets, list) or not assets:
        raise ValueError('Thiếu hồ sơ quyền của hình/âm thanh/tư liệu')
    for asset in assets:
        if not isinstance(asset, dict) or asset.get('status') != 'cleared' or not all(asset.get(k) for k in ['id','type','rights_basis','rights_evidence','allowed_platforms']):
            raise ValueError('Tư liệu còn thiếu căn cứ hoặc phạm vi quyền')
    checks = data.get('platform_checks')
    if not isinstance(checks, list) or not checks:
        raise ValueError('Chưa có kiểm tra chính sách theo nền tảng')
    for item in checks:
        if not isinstance(item, dict) or not item.get('platform') or not public_url(item.get('policy_url')):
            raise ValueError('Thiếu nguồn chính sách nền tảng')
        if item.get('ai_disclosure') not in ['required_applied','not_required_documented']:
            raise ValueError('Chưa xác định/áp dụng công khai AI')
        checked_at(item.get('checked_at'), now)
        if any(item['platform'] not in a['allowed_platforms'] for a in assets):
            raise ValueError('Có tư liệu không được ghi quyền dùng trên nền tảng dự kiến')
