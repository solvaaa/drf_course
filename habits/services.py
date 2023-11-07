import json
from datetime import datetime, timedelta, date

from django_celery_beat.models import IntervalSchedule, PeriodicTask, CrontabSchedule, ClockedSchedule

from habits.models import Habit


def create_periodic_task(user, habit):
    frequency = habit.frequency
    time = str(habit.time)
    hour, minute, seconds = time.split(':')
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=hour,
        minute=minute,
        day_of_month=f'*/{frequency}'
    )

    text = f'{user.telegram_handle},\n' \
           f'настало время ({habit.time}) сделать вашу привычку ' \
           f'{habit.name}.\n' \
           f'Действие: {habit.action}.\n' \
           f'Место: {habit.place}'
    chat_id = user.chat_id
    try:
        task = PeriodicTask.objects.get(name=f'Task for {habit.id}, user {user.id}')
        task.crontab = schedule
        task.args=json.dumps([chat_id, text])
        task.expires=datetime.now() + timedelta(days=300)
        task.save()

    except PeriodicTask.DoesNotExist:
        task = PeriodicTask.objects.create(
            crontab=schedule,
            name=f'Task for {habit.id}, user {user.id}',
            task='habits.tasks.send_reminder',
            args=json.dumps([chat_id, text]),
            expires=datetime.now() + timedelta(days=300)
        )
        habit.periodic_task = task
        habit.save()


def delete_periodic_task(habit):
    task = habit.periodic_task
    if task:
        task.delete()


def create_tasks_for_user(user):
    habits = Habit.objects.filter(user=user)
    for habit in habits:
        create_periodic_task(user, habit)
