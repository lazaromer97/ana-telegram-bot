import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler


def ayuda(update, context):
    update.message.reply_text("La ayuda estara disponible aqui")


if __name__ == '__main__':
    load_dotenv()

    TOKEN = os.getenv('TOKEN')

    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('ayuda', ayuda))

    updater.start_polling()
    updater.idle()
