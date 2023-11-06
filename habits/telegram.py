import requests

from config.settings import TELEGRAM_BOT_TOKEN

TELEGRAM_BOT_URL = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN


def get_update():
    response = requests.get(TELEGRAM_BOT_URL + 'getUpdates')
    if response.status_code != 200:
        raise ConnectionError('Telegram bot didnt connect')
    else:
        return response.json()


def send_message(chat_id, text):
    response = requests.post(TELEGRAM_BOT_URL + 'sendMessage')
    if response.status_code != 200:
        raise ConnectionError('Telegram bot didnt connect')
    else:
        return response.json()
