#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
#https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot.py

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os
import telegram
import telebot
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler,CallbackQueryHandler
from dotenv import load_dotenv
from telegram import  InlineKeyboardButton,InlineKeyboardMarkup, Video, Bot
from telegram.update import Update
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
load_dotenv()
API_KEY = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
tb = telebot.TeleBot(API_KEY)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    files = {'video':open('surprise.mp4','rb')}
    resp = requests.post('https://api.telegram.org/bot'+ API_KEY +'/sendVideo?chat_id=' + CHAT_ID, files = files)
    telegram.Video(file_id='surprise.mp4',file_unique_id='aaa',width=1,height=1,duration=1)
    
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def bernie(update, context): 
    update.message.reply_text('BERNIE BERNIE')

def wash(update, context):
    keyboard = [[InlineKeyboardButton("Machine One", callback_data='Machine One')], [InlineKeyboardButton("Machine Two", callback_data='Machine Two')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please Select:', reply_markup=reply_markup)

def button(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected button: {query.data}")

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(API_KEY, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("bernie", bernie))
    dp.add_handler(CommandHandler("wash",wash))
    dp.add_handler(CallbackQueryHandler(button))
    

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()