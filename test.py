import telebot
import datetime
import time

BOT_TOKEN = '8259339256:AAFLtjDITQTo1-W2yigShG7QSMW1vzICMgI'
CHANNEL_USERNAME = '@testtgforme'

bot = telebot.TeleBot(BOT_TOKEN)

print("🚀 Бот запущено. Щохвилинне надсилання повідомлень...")

for i in range(5):  # Надішле 5 повідомлень (по 1 на хвилину)
    try:
        now = datetime.datetime.now().strftime('%H:%M:%S')
        bot.send_message(CHANNEL_USERNAME, f"[{now}] Тестове повідомлення #{i+1}")
        print(f"✅ Надіслано повідомлення #{i+1}")
    except Exception as e:
        print(f"❌ Помилка: {e}")
    time.sleep(60)  # Затримка 1 хвилина
