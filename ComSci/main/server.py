import os
import sys
import logging
import tg
import requests
import socket

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, InlineQueryHandler,CallbackQueryHandler

from requests.api import get
from requests.models import ChunkedEncodingError

# For telegram bot
load_dotenv()
API_KEY = os.getenv('API_KEY')
GROUP_ID = os.getenv('GROUP_ID')
# For socket port.
HOST = 'localhost'
PORT = 8080
PHOTO_PATH = 'testimage.png'


def button(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected button: {query.data}")
    if query.data == 'Dry again':
        # insert command to send signl to adruino
        print('signal')
        pass


def main():
    # vvv Testing Version vvv
    # updater = Updater(API_KEY, use_context=True)
    # dp = updater.dispatcher
    # dp.add_handler(CallbackQueryHandler(button))
    # while True:
    #     updater.start_polling()
    #     testInput = input("Input function. \n")
    #     if testInput == '1':    
    #         test = tg.TelegramClass()
    #         test.confirm_dryness(PHOTO_PATH)
    #     updater.idle()
    # ^^^ This update.idle() is causing some problem, cannot ctrl + c to kill terminal.
    # it works for the version below but not the testing verion, idk why.

    print(" Choose one")

    # vvv  This works but the conditional statement not added yet vvv
    # # Create the Updater and pass it your bot's token.
    # # Make sure to set use_context=True to use the new context based callbacks
    # # Post version 12 this will no longer be necessary
    # updater = Updater(API_KEY, use_context=True)
    # # Get the dispatcher to register handlers
    # dp = updater.dispatcher
    # dp.add_handler(CallbackQueryHandler(button))

    # # Start the Bot
    # updater.start_polling()
    # # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # # SIGTERM or SIGABRT. This should be used most of the time, since
    # # start_polling() is non-blocking and will stop the bot gracefully.
    # updater.idle()
    
   

if __name__ == '__main__':
    main()