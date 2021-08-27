import os
import telegram
import telebot
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, InlineQueryHandler,CallbackQueryHandler


# For telegram bot
load_dotenv()
API_KEY = os.getenv('API_KEY')
GROUP_ID = os.getenv('GROUP_ID')


class TelegramClass:
    def __init__(self) -> None:
        self.token = API_KEY
        self.chat_ID = GROUP_ID

    def alert_nurse(self,machine): # When dry,wash,sterlize is completed
        print("Alert - Machine {0} is ready for collection.".format(self.machine))

    def alert_error(self,step,machine): # When error occurs at any step
        print("Error - {0} is not complete at Machine {1}".format(self.step,self.machine))

    def confirm_dryness(self,image):
        bot = telegram.Bot(token=API_KEY)
        #bot.send_photo(chat_id = GROUP_ID, photo=open(image,'rb'))
        keyboard = [[InlineKeyboardButton("Yes, please dry again", callback_data='Dry again')], [InlineKeyboardButton("No, do not dry again", callback_data='Dont dry again')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=GROUP_ID,text = "Please select:", reply_markup=reply_markup)
        