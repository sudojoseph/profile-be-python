import os
import requests


class Telegram:
    def send(self, message):
        URL = 'https://telegram-loggin-microservice-05d27d17ae1b.herokuapp.com/'
        json = {"telegramBotToken": os.getenv("TELEGRAM_BOT_TOKEN"),
                "chatId": os.getenv("TELEGRAM_BOT_CHAT_ID"),
                "message": message}
        headers = {'Content-Type': 'application/json',
                         'x-api-key': os.getenv('TELEGRAM_LOGGER_API_KEY')}
        try:
            requests.post(URL, json=json, headers=headers)
        except Exception as e:
            print(e)
        return 'success'