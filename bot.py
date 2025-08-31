from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Токен берём из переменной окружения (безопасно!)
TOKEN = os.getenv("8257985518:AAGlJSJb4LtwUZ_tGlUem1UERC1jbtIeOvg")

# Ссылка на твой GitHub Pages сайт с radio.html
WEBAPP_URL = "https://yourusername.github.io/telegram-radio/radio.html"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("▶️ Слушать радио", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎶 Привет! Я радио-бот.\n\nНажми кнопку ниже, чтобы слушать радио:",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
