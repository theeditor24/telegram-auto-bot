import time
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@corn_adult_content"

messages = [
    "🔥 New music dropping soon!",
    "🎧 Stay tuned for fresh vibes!",
    "💫 Follow for daily lofi energy!",
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
    time.sleep(600)
