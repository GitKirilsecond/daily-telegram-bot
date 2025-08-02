import telebot
from datetime import datetime

BOT_TOKEN = '8259339256:AAFLtjDITQTo1-W2yigShG7QSMW1vzICMgI'
CHANNEL_USERNAME = '@testtgforme'

bot = telebot.TeleBot(BOT_TOKEN)

try:
    now = datetime.now().strftime('%H:%M:%S')
    message = f"[{now}] я працюю автоматично"
    bot.send_message(CHANNEL_USERNAME, message)
    print(f"✅ Повідомлення надіслано: {message}")
except Exception as e:
    print(f"❌ Помилка: {e}")
