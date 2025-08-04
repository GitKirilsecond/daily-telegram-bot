import telebot
import datetime

BOT_TOKEN = '8259339256:AAFLtjDITQTo1-W2yigShG7QSMW1vzICMgI'
CHANNEL_USERNAME = '@testtgforme'

now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)  # Київський час
if now.hour == 12 and 30 <= now.minute <= 59:
    text = f"[{now.strftime('%H:%M:%S')}] Повідомлення через Render кожні 5 хвилин (12:30–12:59)"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHANNEL_USERNAME, 'text': text}
    requests.post(url, data=payload)