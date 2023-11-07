import json
from datetime import datetime, timedelta

import requests
from celery import shared_task
from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule

from config.settings import TELEGRAM_BOT_TOKEN
import habits.telegram as telegram
from habits.services import create_tasks_for_user
from users.models import User

TELEGRAM_BOT_URL = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN


# Создаем интервал для повтора
@shared_task
def task1(id):
    print(f'TASK{id} DONE @!!!!!!!!!!!!!!!!!!')


@shared_task
def get_telegram_updates():
    welcome_text = 'С этого момента я буду напоминать о ваших привычках'
    not_authorized_text = 'Для использования бота зарегистрируйтесь на ' \
                          'нашем сайте'

    updates = telegram.get_update()
    max_update_id = 0
    new_messages = []
    if len(updates['result']):
        for update in updates['result']:
            update_id = update['update_id']
            if update_id > max_update_id:
                max_update_id = update_id
            message = update['message']
            if update['message']['text'] == '/start':
                username = message['chat']['username']
                chat_id = message['chat']['id']
                new_messages.append({'username': username, 'chat_id':chat_id})
        telegram.get_update(offset=max_update_id + 1)
        for new_message in new_messages:
            username = new_message['username']
            chat_id = new_message['chat_id']
            try:
                user = User.objects.get(telegram_handle=username)
            except User.DoesNotExist:
                telegram.send_message(chat_id, not_authorized_text)
            else:
                user.chat_id = chat_id
                user.save()
                telegram.send_message(chat_id, welcome_text)
                create_tasks_for_user(user)




@shared_task
def send_reminder(chat_id, text):
    telegram.send_message(chat_id, text)

