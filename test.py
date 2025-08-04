import telebot
import datetime

BOT_TOKEN = '8259339256:AAFLtjDITQTo1-W2yigShG7QSMW1vzICMgI'
CHANNEL_USERNAME = '@testtgforme'

bot = telebot.TeleBot(BOT_TOKEN)
now = datetime.datetime.now()

# Якщо зараз між 13:30 і 14:30 — надсилаємо повідомлення кожні 5 хвилин
if now.hour == 13 and 30 <= now.minute <= 59:
    msg = now.strftime("[%H:%M:%S]") + " 🧪 Тест кожні 5 хв"
    bot.send_message(CHANNEL_USERNAME, msg)
