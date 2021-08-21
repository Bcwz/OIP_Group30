import logging
import os
import telegram
import telebot
import requests
import datetime

from requests.api import get
from requests.models import ChunkedEncodingError
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler,CallbackQueryHandler, ConversationHandler,CallbackContext
from dotenv import load_dotenv
from telegram import  InlineKeyboardButton,InlineKeyboardMarkup, Video, Bot
from telegram.update import Update

load_dotenv()
API_KEY = os.getenv('API_KEY')
#CHAT_ID = os.getenv('CHAT_ID')
GROUP_ID = os.getenv('GROUP_ID')



def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(API_KEY, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    updater.bot.sendMessage(chat_id = GROUP_ID,
    text = 'Machine {0} is ready - {1}'.format("ONE", datetime.datetime.now().isoformat(' ','seconds')))
    






    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()