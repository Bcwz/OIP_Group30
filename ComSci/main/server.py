import sys
import logging
import os
import telegram
import telebot
import requests
import socket

from requests.api import get
from requests.models import ChunkedEncodingError
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler,CallbackQueryHandler, ConversationHandler,CallbackContext
from dotenv import load_dotenv
from telegram import  InlineKeyboardButton,InlineKeyboardMarkup, Video, Bot
from telegram.update import Update
from flask import url_for

# For telegram bot
load_dotenv()
API_KEY = os.getenv('API_KEY')
GROUP_ID = os.getenv('GROUP_ID')
# For socket port.
HOST = 'localhost'
PORT = 8080


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(API_KEY, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher


    
    # Alert user for status update
    # updater.bot.sendMessage(chat_id = GROUP_ID,
    # text = 'Machine {0} is ready - {1}'.format("ONE", datetime.datetime.now().isoformat(' ','seconds')))



    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()




    #Do a while True to listen for API calls, then send message to telegram based on api calls
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        conn , addr = s.accept()
        with conn:
            print("Connect by", addr)
            while True:
                data = conn.recv(1024)
                if data == 'start':
                    #Sensor class, start_cleaning()
                    pass
                elif data == 'stop':
                    #Kill signal
                    pass
                if not data:
                    break
                conn.sendall(data)

            


if __name__ == '__main__':
    main()