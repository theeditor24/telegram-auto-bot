import time
import requests
import os
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@corn_adult_content"

messages = [
    "New video dropping soon... stay ready 👀🔥",
    "Some secrets are too good to stay hidden 🔥 @sexxy_korean_girls",
    "Next post is gonna be crazy... coming shortly 🔥",
    "If you like this... you'll LOVE what's there 💋 @sexxy_korean_girls",
    "Uploading something special... don't go anywhere 😏",
    "You deserve better content than this 😉 👉 @sexxy_korean_girls",
    "Fresh content is on the way... stay tuned 👀",
    "New drop in a few minutes... get ready 😈"
]

def send_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": messages[int(time.time()) % len(messages)]
    }
    requests.post(url, data=data)

while True:
    send_message()
    print("Message sent!")
    delays = [1200, 1800, 30000, 3600, 7200]
    time.sleep(random.choice(delays))
