"""
Radar Agent - Ann Place
Quet tin tuc AI, design, heritage, culture moi sang
Gui digest vao Discord #radar
"""

import os
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone

DISCORD_WEBHOOK = os.environ["DISCORD_RADAR_WEBHOOK"]

FEEDS = [
    {"name": "MIT Tech Review - AI", "url": "https://www.technologyreview.com/feed/", "tag": "AI"},
    {"name": "Google AI Blog", "url": "https://blog.google/technology/ai/rss/", "tag": "AI"},
    {"name": "Eye on Design (AIGA)", "url": "https://eyeondesign.aiga.org/feed/", "tag": "Design"},
    {"name": "Creative Boom", "url": "https://www.creativeboom.com/feed/", "tag": "Design"},
    {"name": "Hyperallergic", "url": "https://hyperallergic.com/feed/", "tag": "Art/Heritage"},
    {"name": "The Art Newspaper", "url": "https://www.theartnewspaper.com/rss", "tag": "Art/Heritage"},
]

def fetch_rss(url, max_items=2):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "AnnPlace-Radar/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode("utf-8", errors="ignore")
        items = []
        import re
        entries = re.findall(r"<item>(.*?)</item>", content, re.DOTALL)
        for entry in entries[:max_items]:
            title = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", entry)
            link = re.search(r"<link>(.*?)</link>", entry)
            if title and link:
                items.append((title.group(1).strip(), link.group(1).strip()))
        return items
    except Exception as e:
        print(f"RSS fetch error for {url}: {e}")
        return []

def send_discord(content):
    data = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(
        DISCORD_WEBHOOK,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            print(f"Discord response status: {r.status}")
            return r.status
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        print(f"Discord error {e.code}: {body}")
        raise

def main():
    today = datetime.now(timezone.utc).strftime("%d/%m/%Y")
    lines = ["## Radar - " + today + "\n"]
    found_any = False
    for feed in FEEDS:
        items = fetch_rss(feed["url"])
        if items:
            found_any = True
            lines.append("**" + feed["tag"] + " - " + feed["name"] + "**")
            for title, link in items:
                if len(title) > 80:
                    title = title[:77] + "..."
                lines.append("- [" + title + "](" + link + ")")
            lines.append("")
    if not found_any:
        lines.append("_(Khong lay duoc tin hom nay)_")
    message = "\n".join(lines)
    if len(message) > 1900:
        message = message[:1900] + "\n_...(xem them)_"
    send_discord(message)
    print("Radar sent: " + str(len(message)) + " chars")

if __name__ == "__main__":
    main()
