import json
from datetime import datetime, timedelta

from django_celery_beat.models import IntervalSchedule, PeriodicTask

from habits.models import Habit


def create_periodic_task(user, habit):

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=20,
        period=IntervalSchedule.SECONDS,
    )

    text = f'{user.telegram_handle},\n' \
           f' настало время сделать вашу привычку {habit.name}.\n' \
           f' Действие: {habit.action}'
    chat_id = user.chat_id

    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Task for {habit.id}, user {user.id}',
        task='habits.tasks.send_reminder',
        args=json.dumps([chat_id, text]),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )


def create_tasks_for_user(user):
    habits = Habit.objects.filter(user=user)
    for habit in habits:
        create_periodic_task(user, habit)