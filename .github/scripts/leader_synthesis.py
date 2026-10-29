"""
Leader Synthesis — Ann Place (Claude / Einstein)
Chay 17:00 VN (10:00 UTC) moi ngay qua GitHub Actions
Doc output cua Radar + Art + Opportunity → tong hop → gui Discord #general
"""

import os
import json
import re
import http.client
import ssl
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent.parent  # repo root

OUTPUT_FILES = {
    "radar":       ROOT / "agents" / "radar"       / "output" / "output.md",
    "art":         ROOT / "agents" / "art"          / "output" / "output.md",
    "opportunity": ROOT / "agents" / "opportunity"  / "output" / "output.md",
}

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK") or (
    json.loads((ROOT / "config" / "webhooks.json").read_text())["general"]
)

# ── Read agent outputs ────────────────────────────────────────────────────────

def read_output(key: str) -> str:
    path = OUTPUT_FILES[key]
    if path.exists():
        text = path.read_text(encoding="utf-8").strip()
        return text if text else None
    return None


def extract_top_lines(text: str, n: int = 3) -> list[str]:
    """Lay n dong co noi dung (bo header, blank lines)."""
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            # Strip markdown link syntax for cleaner preview
            clean = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", stripped)
            clean = re.sub(r"^[-*•]\s*", "• ", clean)
            lines.append(clean[:120])
        if len(lines) >= n:
            break
    return lines


def extract_deadline_alerts(text: str) -> list[str]:
    """Tim dong co tu khoa deadline/han nop trong vong 7 ngay."""
    alerts = []
    today = datetime.now(timezone(timedelta(hours=7))).date()  # VN time
    for line in text.splitlines():
        if re.search(r"deadline|hạn nộp|hạn đăng ký|due|expires?", line, re.IGNORECASE):
            # Try to find a date in the line
            date_match = re.search(r"(\d{1,2})[/\-](\d{1,2})(?:[/\-](\d{2,4}))?", line)
            if date_match:
                day, month = int(date_match.group(1)), int(date_match.group(2))
                year = int(date_match.group(3)) if date_match.group(3) else today.year
                if year < 100:
                    year += 2000
                try:
                    deadline_date = today.replace(year=year, month=month, day=day)
                    days_left = (deadline_date - today).days
                    if 0 <= days_left <= 7:
                        clean = line.strip()[:100]
                        alerts.append(f"🚨 {clean} _(còn {days_left} ngày)_")
                except ValueError:
                    pass
            else:
                # No parseable date but has deadline keyword — include anyway
                alerts.append("⚠️ " + line.strip()[:100])
    return alerts[:3]  # max 3 alerts


# ── Build report ─────────────────────────────────────────────────────────────

def build_report() -> str:
    vn_now = datetime.now(timezone(timedelta(hours=7)))
    date_str = vn_now.strftime("%d/%m/%Y")
    time_str = vn_now.strftime("%H:%M")

    radar_raw       = read_output("radar")
    art_raw         = read_output("art")
    opportunity_raw = read_output("opportunity")

    sections = [f"🌙 **Báo cáo ngày {date_str} — Ann Place**\n"]

    # ── Radar ────────────────────────────────────────────────────────────────
    if radar_raw:
        top = extract_top_lines(radar_raw, n=3)
        sections.append("📡 **Radar hôm nay** (top tin):")
        for line in top:
            sections.append(line)
    else:
        sections.append("📡 **Radar:** _(chưa có update hôm nay)_")
    sections.append("")

    # ── Art / SaLu ───────────────────────────────────────────────────────────
    if art_raw:
        top = extract_top_lines(art_raw, n=2)
        sections.append("🎨 **SaLu content hôm nay:**")
        for line in top:
            sections.append(line)
    else:
        sections.append("🎨 **SaLu:** _(chưa có update hôm nay)_")
    sections.append("")

    # ── Opportunity ──────────────────────────────────────────────────────────
    if opportunity_raw:
        top = extract_top_lines(opportunity_raw, n=2)
        sections.append("🔬 **Cơ hội nổi bật:**")
        for line in top:
            sections.append(line)
        # Deadline alerts
        alerts = extract_deadline_alerts(opportunity_raw)
        for alert in alerts:
            sections.append(alert)
    else:
        sections.append("🔬 **Cơ hội:** _(chưa có update hôm nay)_")
    sections.append("")

    # ── Recommendation ───────────────────────────────────────────────────────
    # Simple priority logic: deadline alert → opportunity → art → radar
    rec = _pick_recommendation(radar_raw, art_raw, opportunity_raw)
    sections.append(f"⚡ **Claude khuyến nghị:**\n→ {rec}")
    sections.append("")

    sections.append(f"---\n*Generated by Ann Place AI Office • {time_str} VN*")

    message = "\n".join(sections)

    # Discord limit: 2000 chars
    if len(message) > 1950:
        message = message[:1950] + "\n_...(xem thêm trong repo)_"

    return message


def _pick_recommendation(radar, art, opportunity) -> str:
    # 1. Urgent deadline in opportunity
    if opportunity:
        alerts = extract_deadline_alerts(opportunity)
        if alerts:
            return "Kiểm tra deadline cơ hội — " + alerts[0].replace("🚨 ", "").replace("⚠️ ", "")

    # 2. Opportunity exists
    if opportunity:
        first = extract_top_lines(opportunity, n=1)
        if first:
            return "Xem xét cơ hội: " + first[0].lstrip("• ")

    # 3. SaLu content ready
    if art:
        first = extract_top_lines(art, n=1)
        if first:
            return "SaLu có concept mới — cân nhắc đăng hoặc lên lịch: " + first[0].lstrip("• ")

    # 4. Radar has something
    if radar:
        first = extract_top_lines(radar, n=1)
        if first:
            return "Đọc bản tin nổi bật: " + first[0].lstrip("• ")

    return "Không có agent nào push output hôm nay — kiểm tra lại lịch chạy của team."


# ── Send to Discord ───────────────────────────────────────────────────────────

def send_discord(message: str, webhook_url: str):
    payload = json.dumps({
        "content": message,
        "username": "Ann Place — Leader"
    }).encode("utf-8")

    host = "discord.com"
    path = webhook_url.replace("https://discord.com", "")
    ctx = ssl.create_default_context()
    conn = http.client.HTTPSConnection(host, context=ctx, timeout=15)
    headers = {
        "Content-Type": "application/json",
        "Content-Length": str(len(payload)),
        "User-Agent": "AnnPlace-Leader/1.0",
    }
    conn.request("POST", path, body=payload, headers=headers)
    resp = conn.getresponse()
    body = resp.read().decode("utf-8", errors="ignore")
    print(f"Discord response {resp.status}: {body[:200]}")
    if resp.status not in (200, 204):
        raise RuntimeError(f"Discord webhook failed {resp.status}: {body}")
    return resp.status


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=== Ann Place Leader Synthesis ===")
    report = build_report()
    print("--- Report preview ---")
    print(report)
    print("--- Sending to Discord ---")
    send_discord(report, WEBHOOK_URL)
    print("Done.")


if __name__ == "__main__":
    main()
