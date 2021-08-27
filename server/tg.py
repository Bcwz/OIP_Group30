import os
import telegram

# For telegram bot
API_KEY = "1837082029:AAHU48tAh94AD8bWQfkSiZXfOJug0Mw4FEI"
GROUP_ID = "-1001501180878"


class TelegramClass:
    def __init__(self) -> None:
        self.token = API_KEY
        self.chat_ID = GROUP_ID

    def alert_nurse(self):
        bot = telegram.Bot(token=API_KEY)
        bot.send_message(chat_id=GROUP_ID,
                         text="Alert - Syringes are ready for collection.")
