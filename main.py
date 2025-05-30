
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

# Пример базы продуктов
products = {
    "k-213": "K-213 — нейтральное средство для ручной мойки посуды. pH: 7.5. Упаковка: 1/5/10 л.",
    "h-110": "H-110 — гелеобразное кислотное средство для туалетов. pH: <1.0."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот-консультант по продуктам Тайгета.\nНапиши артикул, например: K-213")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напиши артикул продукта, и я расскажу о нём всё, что знаю.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    reply = products.get(text, "Не нашёл такой продукт. Попробуй другой артикул.")
    await update.message.reply_text(reply)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
