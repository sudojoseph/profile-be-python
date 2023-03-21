import telepot
import os
import asyncio


class Telegram:
    def __init__(self):
        self.bot = telepot.Bot(os.getenv("TELEGRAM_BOT_TOKEN"))


    def send(self, message):
        self.bot.sendMessage(os.getenv("TELEGRAM_BOT_CHAT_ID"), message)
        return 'success'
