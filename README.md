# 🎧 Telegram Radio Bot

Бот для прослушивания онлайн-радио прямо в Telegram.

## 🚀 Установка и запуск локально

1. Склонируй репозиторий:
   ```bash
   git clone https://github.com/yourusername/telegram-radio-bot.git
   cd telegram-radio-bot
   ```

2. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запусти бота (перед этим установи переменную окружения с токеном):
   ```bash
   export TOKEN=твой_токен
   python bot.py
   ```

## ☁️ Деплой на Render

1. Создай новый Web Service на [Render](https://render.com).  
2. В настройках укажи:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
3. Добавь переменную окружения:
   ```
   TOKEN = твой_токен
   ```
4. Нажми Deploy — бот запустится 24/7.

---

📌 Перед запуском замени ссылку `WEBAPP_URL` в `bot.py` на свой GitHub Pages с `radio.html`!
