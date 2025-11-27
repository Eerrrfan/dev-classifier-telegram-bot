import os
import joblib
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

MODEL_PATH = "programmer_model.joblib"
model = joblib.load(MODEL_PATH)



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Hi! 👋\n"
        "Send me any sentence and I'll guess whether the person is a *developer* or *non-developer*.\n\n"
        "Type /help for more info."
    )
    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Just send a message like:\n"
        "- 'I use Python and Docker at work'\n"
        "- 'I love watching movies with my friends'\n\n"
        "and I'll classify it as DEV or NONDEV."
    )
    await update.message.reply_text(text)


async def classify_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    pred = model.predict([user_text])[0]

    if pred == "dev":
        reply = "💻 This person is likely a *PROGRAMMER*."
    else:
        reply = "🙂 This person is likely *NOT* a programmer."

    await update.message.reply_text(reply, parse_mode="Markdown")



def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "telegram-token")

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))    #/start
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, classify_message)
    )

    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
