import telebot
from datetime import datetime
import pytz

# 🔐 Дані твого бота
BOT_TOKEN = "8259339256:AAFLtjDITQTo1-W2yigShG7QSMW1vzICMgI"
CHANNEL_USERNAME = "@testtgforme"

# ⏱️ Підтримка часового поясу Києва
kyiv_tz = pytz.timezone('Europe/Kyiv')
now_kyiv = datetime.now(kyiv_tz).strftime('%H:%M:%S')

# 📩 Повідомлення
message = f"🕯️ Оголошено хвилину мовчання в памʼять загиблих захисників України.\n\nСлава Героям! 🇺🇦"

# 📤 Надсилання повідомлення
bot = telebot.TeleBot(BOT_TOKEN)
bot.send_message(CHANNEL_USERNAME, f"[{now_kyiv}] {message}")
