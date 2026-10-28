"""
General Agent — Ann Place · Điều phối + Kế toán
Chạy mỗi Thứ Hai 8:00 UTC = 15:00 VN
Post báo cáo tuần lên #general:
  - Tóm tắt agents đã chạy tuần qua
  - Xu hướng nổi bật từ Radar
  - Cơ hội đáng chú ý
  - Ước tính usage GitHub Actions (miễn phí, theo dõi phút)
  - Việc cần bạn quyết định tuần này

KHÔNG tự nộp hồ sơ, không chi tiền, không gửi email khi chưa được giao quyền
"""

import json
import datetime
import http.client
import ssl
import os
import re

_cfg = json.load(open("config/webhooks.json"))
DISCORD_WEBHOOK = _cfg["general"]


def send_discord(content):
    host = "discord.com"
    path = DISCORD_WEBHOOK.replace("https://discord.com", "")
    if len(content) > 1900:
        content = content[:1900] + "\n…*(tiếp theo tuần sau)*"
    payload = json.dumps({"content": content, "username": "Ann Place · Điều phối"})
    ctx = ssl.create_default_context()
    conn = http.client.HTTPSConnection(host, context=ctx, timeout=10)
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (https://github.com/thuyanhdo238/ann-place238, 1.0)",
        "Content-Length": str(len(payload.encode("utf-8"))),
    }
    conn.request("POST", path, body=payload, headers=headers)
    resp = conn.getresponse()
    body = resp.read().decode("utf-8", errors="ignore")
    print(f"Discord response {resp.status}: {body}")
    if resp.status not in (200, 204):
        raise Exception(f"Discord error {resp.status}: {body}")
    return resp.status


# Lịch chạy các agent (UTC) — dùng để báo cáo trạng thái
AGENT_SCHEDULE = [
    {"name": "Radar", "channel": "#radar", "time_utc": "0:00", "time_vn": "7:00", "days": "hằng ngày"},
    {"name": "Chance", "channel": "#chance", "time_utc": "1:00", "time_vn": "8:00", "days": "hằng ngày"},
    {"name": "Art Sympathy (SaLu)", "channel": "#art", "time_utc": "2:00", "time_vn": "9:00", "days": "hằng ngày"},
    {"name": "Cơ hội", "channel": "#radar", "time_utc": "6:00", "time_vn": "13:00", "days": "hằng ngày"},
    {"name": "Điều phối (báo cáo)", "channel": "#general", "time_utc": "8:00 T2", "time_vn": "15:00 T2", "days": "Thứ Hai"},
]

# GitHub Actions free tier: 2000 phút/tháng cho private repo
# Mỗi job chạy ~1 phút → ước tính
GITHUB_ACTIONS_FREE_MINUTES = 2000


def estimate_monthly_usage():
    """Ước tính phút GitHub Actions dùng trong tháng"""
    daily_agents = 4   # radar, chance, art, opportunity
    weekly_agents = 1  # general (thứ hai)
    days_in_month = 30
    weeks_in_month = 4
    minutes_per_run = 1  # ước tính

    daily_total = daily_agents * days_in_month * minutes_per_run
    weekly_total = weekly_agents * weeks_in_month * minutes_per_run
    total = daily_total + weekly_total
    pct = round(total / GITHUB_ACTIONS_FREE_MINUTES * 100, 1)
    return total, pct


def get_week_range():
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    sunday = monday + datetime.timedelta(days=6)
    return monday.strftime("%d/%m"), sunday.strftime("%d/%m/%Y")


def read_pipeline():
    """Đọc pipeline.md và phân loại theo trạng thái"""
    pipeline_path = "pipeline.md"
    if not os.path.exists(pipeline_path):
        return None
    with open(pipeline_path, encoding="utf-8") as f:
        content = f.read()

    status_map = {
        "[>]": ("đang làm", "🔵"),
        "[?]": ("chờ quyết định", "🟡"),
        "[!]": ("cần sửa", "🔴"),
        "[ ]": ("chưa bắt đầu", "⚪"),
        "[x]": ("xong", "✅"),
    }

    in_progress, waiting, needs_fix = [], [], []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [>]"):
            in_progress.append(stripped[5:].strip())
        elif stripped.startswith("- [?]"):
            waiting.append(stripped[5:].strip())
        elif stripped.startswith("- [!]"):
            needs_fix.append(stripped[5:].strip())

    return {"in_progress": in_progress, "waiting": waiting, "needs_fix": needs_fix}


def build_message():
    week_start, week_end = get_week_range()
    today_str = datetime.date.today().strftime("%d/%m/%Y")
    monthly_minutes, pct = estimate_monthly_usage()

    lines = []
    lines.append(f"# 🗂️ Báo cáo tuần — Ann Place")
    lines.append(f"*Tuần {week_start} – {week_end} · Điều phối tổng hợp*\n")

    # Pipeline
    pipeline = read_pipeline()
    if pipeline:
        lines.append("## 📋 Pipeline công việc")
        if pipeline["needs_fix"]:
            lines.append("**🔴 Cần sửa:**")
            for item in pipeline["needs_fix"]:
                lines.append(f"  • {item}")
        if pipeline["waiting"]:
            lines.append("**🟡 Chờ bạn quyết định:**")
            for item in pipeline["waiting"]:
                lines.append(f"  • {item}")
        if pipeline["in_progress"]:
            lines.append("**🔵 Đang làm:**")
            for item in pipeline["in_progress"]:
                lines.append(f"  • {item}")
        if not any([pipeline["needs_fix"], pipeline["waiting"], pipeline["in_progress"]]):
            lines.append("*Không có việc nào đang chạy — kiểm tra pipeline.md*")

    # Trạng thái các agent
    lines.append("\n## ✅ Agents đang chạy")
    for a in AGENT_SCHEDULE:
        lines.append(f"• **{a['name']}** → {a['channel']} lúc {a['time_vn']} ({a['days']})")

    # Usage tracking
    lines.append("\n## 📊 Ước tính tài nguyên")
    lines.append(f"• GitHub Actions: ~{monthly_minutes} phút/tháng ≈ **{pct}% free tier** (giới hạn 2.000 phút)")
    lines.append(f"• Chi phí hosting: **$0**")
    lines.append(f"• Claude/ChatGPT: gói cố định — agents không dùng API, không phát sinh thêm")
    lines.append("• ⚠️ *Số trên là ước tính, không phải hóa đơn thật*")

    # Ghi chú
    lines.append("\n---")
    lines.append("*Không tự nộp hồ sơ · không gửi email · không chi tiền khi chưa được giao quyền*")
    lines.append(f"*Tự động · {today_str}*")

    return "\n".join(lines)


def main():
    print("General Agent (Điều phối) starting...")
    msg = build_message()
    print(f"Message preview:\n{msg[:300]}...")
    status = send_discord(msg)
    print(f"Done. Status: {status}")


if __name__ == "__main__":
    main()
