import requests

from config.settings import TELEGRAM_BOT_TOKEN

TELEGRAM_BOT_URL = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN


def get_update(offset=None):
    params = {}
    if offset:
        params['offset'] = offset
    response = requests.get(TELEGRAM_BOT_URL + '/getUpdates', params=params)
    print(response.status_code)
    print(response.json())
    if response.status_code != 200:
        raise ConnectionError('Telegram bot didnt connect')
    else:
        return response.json()


def send_message(chat_id, text):
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(TELEGRAM_BOT_URL + '/sendMessage', params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise ConnectionError('Telegram bot didnt connect')
    else:
        return response.json()
