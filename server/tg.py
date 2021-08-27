import os
import telegram
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# For telegram bot
load_dotenv()
API_KEY = os.getenv('API_KEY')
GROUP_ID = os.getenv('GROUP_ID')


class TelegramClass:
    def __init__(self) -> None:
        self.token = API_KEY
        self.chat_ID = GROUP_ID

    def alert_nurse(self):
        bot = telegram.Bot(token=API_KEY)
        bot.send_message(chat_id=GROUP_ID,
                         text="Alert - Syringes are ready for collection.")
