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
    if len(updates):
        for update in updates:
            if update['text'] == '/start':
                username = update['chat']['username']
                chat_id = update['chat']['id']
                user = User.objects.get(telegram_handle=username).exists()
                if user is not None:
                    telegram.send_message(chat_id, welcome_text)
                    create_tasks_for_user(user)
                else:
                    telegram.send_message(chat_id, not_authorized_text)


@shared_task
def send_reminder(chat_id, text):
    telegram.send_message(chat_id, text)

