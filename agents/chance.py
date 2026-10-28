"""
Chance Agent - Ann Place
Moi sang gui 1 cau noi ngau nhien de cam hung ngay moi
Gui vao Discord #chance
Nguon: triet hoc, nghe thuat, thiet ke, van hoa
"""

import os
import json
import http.client
import ssl
import random
from datetime import datetime, timezone

DISCORD_WEBHOOK = os.environ["DISCORD_CHANCE_WEBHOOK"]

# Kho cau noi - triet hoc, nghe thuat, thiet ke, van hoa
QUOTES = [
    ("Simplicity is the ultimate sophistication.", "Leonardo da Vinci"),
    ("Design is not just what it looks like. Design is how it works.", "Steve Jobs"),
    ("Every artist was first an amateur.", "Ralph Waldo Emerson"),
    ("Creativity is intelligence having fun.", "Albert Einstein"),
    ("The details are not the details. They make the design.", "Charles Eames"),
    ("Art enables us to find ourselves and lose ourselves at the same time.", "Thomas Merton"),
    ("To design is to communicate clearly by whatever means you can control or master.", "Milton Glaser"),
    ("Beauty will save the world.", "Fyodor Dostoevsky"),
    ("Everything you can imagine is real.", "Pablo Picasso"),
    ("The purpose of art is washing the dust of daily life off our souls.", "Pablo Picasso"),
    ("Form follows function.", "Louis Sullivan"),
    ("Less is more.", "Ludwig Mies van der Rohe"),
    ("Good design is obvious. Great design is transparent.", "Joe Sparano"),
    ("Color is a power which directly influences the soul.", "Wassily Kandinsky"),
    ("The role of the artist is to ask questions, not answer them.", "Anton Chekhov"),
    ("Art is not what you see, but what you make others see.", "Edgar Degas"),
    ("Typography is the craft of endowing human language with a durable visual form.", "Robert Bringhurst"),
    ("A picture is worth a thousand words.", "Napoleon Bonaparte"),
    ("Have no fear of perfection — you'll never reach it.", "Salvador Dali"),
    ("The job of the artist is always to deepen the mystery.", "Francis Bacon"),
    ("Daring ideas are like chessmen moved forward; they may be beaten, but they may start a winning game.", "Johann Wolfgang von Goethe"),
    ("The principles of true art is not to portray, but to evoke.", "Jerzy Kosinski"),
    ("An idea that is not dangerous is unworthy of being called an idea at all.", "Oscar Wilde"),
    ("It is not the mountain we conquer, but ourselves.", "Edmund Hillary"),
    ("Creativity is allowing yourself to make mistakes. Design is knowing which ones to keep.", "Scott Adams"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Innovation distinguishes between a leader and a follower.", "Steve Jobs"),
    ("Make it simple, but significant.", "Don Draper"),
    ("What we see depends mainly on what we look for.", "John Lubbock"),
    ("A designer knows he has achieved perfection not when there is nothing left to add, but when there is nothing left to take away.", "Antoine de Saint-Exupery"),
    ("Good design is as little design as possible.", "Dieter Rams"),
    ("The main thing is to be moved, to love, to hope, to tremble, to live.", "Auguste Rodin"),
    ("Art is the lie that enables us to realize the truth.", "Pablo Picasso"),
    ("Without deviation from the norm, progress is not possible.", "Frank Zappa"),
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("I have no special talent. I am only passionately curious.", "Albert Einstein"),
    ("Imagination is more important than knowledge.", "Albert Einstein"),
    ("Every child is an artist. The problem is how to remain an artist once we grow up.", "Pablo Picasso"),
    ("Vision is the art of seeing what is invisible to others.", "Jonathan Swift"),
    ("The secret to creativity is knowing how to hide your sources.", "Albert Einstein"),
]

def send_discord(content):
    url = DISCORD_WEBHOOK
    host = "discord.com"
    path = url.replace("https://discord.com", "")
    payload = json.dumps({"content": content, "username": "Ann Place Chance"})
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

def main():
    today = datetime.now(timezone.utc).strftime("%d/%m/%Y")
    quote, author = random.choice(QUOTES)
    message = f"## ✨ Chance - {today}\n\n> *\"{quote}\"*\n> — **{author}**"
    send_discord(message)
    print(f"Chance sent: {author}")

if __name__ == "__main__":
    main()
