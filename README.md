
# Taigeta Telegram Bot

Бот для консультаций по продуктам Тайгета.

## Как развернуть на Render:

1. Создай GitHub-репозиторий и залей туда содержимое этой папки.
2. На сайте [https://dashboard.render.com](https://dashboard.render.com):
   - Нажми **"New Web Service"**
   - Подключи свой GitHub-репозиторий
   - В настройках:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python main.py`
   - В разделе Environment добавь переменную:
     - `BOT_TOKEN` = `твой Telegram токен`

3. Нажми "Deploy" — и бот заработает!
