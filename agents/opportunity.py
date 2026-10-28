"""
Opportunity Agent — Ann Place
Quét cơ hội: hội thảo, triển lãm, call for submissions, remote jobs
Post lên #radar (dùng chung) lúc 6:00 UTC = 13:00 VN
Không tự nộp hồ sơ, không tự cam kết — chỉ báo cáo để bạn quyết định
"""

import json
import datetime
import http.client
import ssl
import urllib.request
import re

_cfg = json.load(open("config/webhooks.json"))
DISCORD_WEBHOOK = _cfg["radar"]  # Gộp vào kênh radar — cơ hội liên quan đến nghiên cứu/xu hướng


def send_discord(content):
    host = "discord.com"
    path = DISCORD_WEBHOOK.replace("https://discord.com", "")
    # Discord limit 2000 chars per message
    if len(content) > 1900:
        content = content[:1900] + "\n…*(xem thêm trên nguồn)*"
    payload = json.dumps({"content": content, "username": "Ann Place · Cơ hội"})
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


def fetch_rss(url, timeout=8):
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; AnnPlaceBot/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"RSS fetch error {url}: {e}")
        return ""


def parse_items(xml, max_items=3):
    items = []
    entries = re.findall(r"<item>(.*?)</item>", xml, re.DOTALL)
    if not entries:
        entries = re.findall(r"<entry>(.*?)</entry>", xml, re.DOTALL)
    for entry in entries[:max_items]:
        title = re.search(r"<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", entry, re.DOTALL)
        link = re.search(r"<link[^>]*>(?:<!\[CDATA\[)?(https?://[^\s<\"]+)", entry, re.DOTALL)
        if not link:
            link = re.search(r'<link[^>]+href="(https?://[^"]+)"', entry)
        title = title.group(1).strip() if title else "(không có tiêu đề)"
        link = link.group(1).strip() if link else ""
        # Clean HTML tags
        title = re.sub(r"<[^>]+>", "", title)
        items.append({"title": title, "link": link})
    return items


# Nguồn cơ hội — ưu tiên design, di sản số, AI sáng tạo, remote
OPPORTUNITY_FEEDS = [
    {
        "label": "🎓 Học thuật / Hội thảo",
        "url": "https://www.cfplist.com/rss/",
        "desc": "Call for Papers & hội thảo quốc tế",
    },
    {
        "label": "🎨 Triển lãm / Call for Submissions",
        "url": "https://www.creativemornings.com/blog.rss",
        "desc": "Creative community calls",
    },
    {
        "label": "💼 Remote Design Jobs",
        "url": "https://remoteok.com/remote-design-jobs.rss",
        "desc": "Việc làm design từ xa",
    },
    {
        "label": "🔬 Research / Heritage",
        "url": "https://dh.network/feed/",
        "desc": "Digital humanities & heritage",
    },
]


def build_message():
    today = datetime.date.today().strftime("%d/%m/%Y")
    weekday = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"][datetime.date.today().weekday()]
    lines = [f"## 🔭 Cơ hội hôm nay — {weekday} {today}\n*Chỉ báo cáo — bạn quyết định có nộp/đăng ký không*\n"]

    found_any = False
    for feed in OPPORTUNITY_FEEDS:
        xml = fetch_rss(feed["url"])
        if not xml:
            continue
        items = parse_items(xml, max_items=2)
        if not items:
            continue
        found_any = True
        lines.append(f"\n**{feed['label']}**")
        for item in items:
            link_part = f" → {item['link']}" if item["link"] else ""
            title = item["title"][:120]
            lines.append(f"• {title}{link_part}")

    if not found_any:
        lines.append("*(Hôm nay không lấy được dữ liệu từ các nguồn — kiểm tra logs)*")

    lines.append("\n---\n*⚠️ Chưa xác minh deadline và điều kiện — hãy kiểm tra trực tiếp nguồn trước khi đăng ký*")
    return "\n".join(lines)


def main():
    print("Opportunity Agent starting...")
    msg = build_message()
    print(f"Message preview:\n{msg[:300]}...")
    status = send_discord(msg)
    print(f"Done. Status: {status}")


if __name__ == "__main__":
    main()
