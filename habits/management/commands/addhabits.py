from django.core.management import BaseCommand

from habits.models import Habit
from random import randint, choice

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = list(User.objects.filter(is_staff=False))
        for i in range(30):
            is_pleasant = bool(randint(0, 1))

            name = f'Привычка {i}'
            if is_pleasant:
                name += ' (приятная)'

            reward = {
                'connected_habit': None,
                'reward': None
            }
            if not is_pleasant:
                if not bool(randint(0, 2)) and \
                        Habit.objects.filter(is_pleasant=True).count():
                    reward['connected_habit'] = Habit.objects.\
                                                filter(is_pleasant=True).\
                                                order_by('?').first()
                else:
                    reward['reward'] = f'Вознаграждение {randint(1, 20)}'

            habit = Habit.objects.create(
                name=name,
                user=choice(users),
                time=f'{randint(0, 23)}:{randint(0, 59)}:00',
                place=f'Место {randint(1, 20)}',
                action=f'Действие {randint(1, 20)}',
                is_pleasant=is_pleasant,
                connected_habit=reward['connected_habit'],
                frequency=randint(1, 7),
                reward=reward['reward'],
                duration=randint(1, 120),
                is_public=not bool(randint(0, 2))
            )
            habit.save()
