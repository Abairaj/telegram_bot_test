
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'telegram_bot.settings'
django.setup()

from telegram.ext import filters
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from telegram import Update
from asgiref.sync import sync_to_async
from django.conf import settings

from home.models import BotData


API_KEY = settings.API_KEY


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hi! I'm a bot, please talk to me!")

@sync_to_async
def save_bot_data(update: Update) -> None:
    BotData.objects.create(
        user_name=update.message.from_user.first_name, json={'text': update.message.text})

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    await save_bot_data(update)
    await update.message.reply_text(f"You said: {text}")


def main():
    application = ApplicationBuilder().token(API_KEY).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
