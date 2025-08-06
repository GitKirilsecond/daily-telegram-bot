import time
import requests
from datetime import datetime

BOT_TOKEN = '8259339256:AAFLtjDITQTo1-W2yigShG7QSMW1vzICMgI'
CHANNEL_USERNAME = '@testtgforme'

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHANNEL_USERNAME,
        'text': text
    }
    requests.post(url, data=payload)

# Тест: 5 повідомлень з інтервалом 10 хв
for i in range(5):
    now = datetime.now().strftime("%H:%M:%S")
    send_message(f"[{now}] Абоба #{i+1}")
    if i < 4:
        time.sleep(600)  # 10 хвилин = 600 секунд
