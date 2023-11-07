from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User

HABIT_DATA = {
    "name": "Привычка 1",
    "place": "Место 1",
    "time": "18:12:00",
    "action": "Действие 1",
    "is_pleasant": False,
    "frequency": 2,
    "reward": "Вознаграждение 6",
    "duration": 97,
    "is_public": False
}


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru',
            first_name='Test',
            last_name='Test'
        )
        self.user.set_password('11qwerty11')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create(self):
        data = HABIT_DATA.copy()

        response = self.client.post(
            '/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        habit = Habit.objects.all().first()
        correct_response = {
            'id': habit.id,
            'name': 'Привычка 1',
            'place': 'Место 1',
            'time': '18:12:00',
            'action': 'Действие 1',
            'is_pleasant': False,
            'frequency': 2,
            'reward': 'Вознаграждение 6',
            'duration': 97,
            'is_public': False,
            'user': self.user.id,
            'connected_habit': None,
            'periodic_task': None
        }
        self.assertTrue(
            Habit.objects.all().exists()
        )
        self.assertEqual(
            response.json(),
            correct_response
        )

    def test_delete(self):
        data = HABIT_DATA.copy()
        habit = Habit.objects.create(user=self.user, **data)

        response = self.client.delete(
            f'/delete/{habit.id}'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertFalse(
            Habit.objects.all().exists()
        )

    def test_list(self):
        data = HABIT_DATA.copy()
        habit = Habit.objects.create(user=self.user, **data)

        response = self.client.get(
            '/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        correct_response = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {'id': habit.id,
                     'name': 'Привычка 1',
                     'place': 'Место 1',
                     'time': '18:12:00',
                     'action': 'Действие 1',
                     'is_pleasant': False,
                     'frequency': 2,
                     'reward': 'Вознаграждение 6',
                     'duration': 97,
                     'is_public': False,
                     'user': self.user.id,
                     'connected_habit': None,
                     'periodic_task': None
                     }
                ]
        }

        self.assertEqual(
            response.json(),
            correct_response
        )

    def test_update(self):
        data = HABIT_DATA.copy()
        data['name'] = 'tester2'
        habit = Habit.objects.create(user=self.user, **data)

        response = self.client.put(
            f'/edit/{habit.id}',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertTrue(
            Habit.objects.all().exists()
        )
        correct_response = {
            'id': habit.id,
            'name': 'tester2',
            'place': 'Место 1',
            'time': '18:12:00',
            'action': 'Действие 1',
             'is_pleasant': False,
            'frequency': 2,
            'reward': 'Вознаграждение 6',
            'duration': 97,
            'is_public': False,
            'user': self.user.id,
            'connected_habit': None,
            'periodic_task': None
        }
        self.assertEqual(
            response.json(),
            correct_response
        )

    def test_retrieve(self):
        data = HABIT_DATA.copy()
        habit = Habit.objects.create(user=self.user, **data)

        response = self.client.get(
            f'/{habit.id}'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        correct_response = {
            'id': habit.id,
            'name': 'Привычка 1',
            'place': 'Место 1',
            'time': '18:12:00',
            'action': 'Действие 1',
            'is_pleasant': False,
            'frequency': 2,
            'reward': 'Вознаграждение 6',
            'duration': 97,
            'is_public': False,
            'user': self.user.id,
            'connected_habit': None,
            'periodic_task': None
        }
        self.assertEqual(
            response.json(),
            correct_response
        )

    def test_public_list(self):
        data = HABIT_DATA.copy()

        user_2 = User.objects.create(
            email='test2@mail.ru',
            first_name='Test2',
            last_name='Test2'
        )
        self.user.set_password('11qwerty11')
        self.user.save()

        habit = Habit.objects.create(user=user_2, **data)

        response = self.client.get(
            f'/public/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        correct_response = {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }
        self.assertEqual(
            response.json(),
            correct_response
        )

        data['is_public'] = True
        habit_public = Habit.objects.create(user=user_2, **data)

        response_true = self.client.get(
            f'/public/'
        )
        self.assertEqual(
            response_true.status_code,
            status.HTTP_200_OK
        )
        correct_response_true = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': habit_public.id,
                        'name': 'Привычка 1',
                        'place': 'Место 1',
                        'time': '18:12:00',
                        'action': 'Действие 1',
                        'is_pleasant': False,
                        'frequency': 2,
                        'reward': 'Вознаграждение 6',
                        'duration': 97,
                        'is_public': True,
                        'user': user_2.id,
                        'connected_habit': None,
                        'periodic_task': None
                    }
                ]
        }
        self.assertEqual(
            response_true.json(),
            correct_response_true
        )

    def test_RewardValidator(self):
        data = HABIT_DATA.copy()
        data['is_pleasant'] = True
        del data['reward']
        pleasant_habit = Habit.objects.create(user=self.user, **data)

        data = HABIT_DATA.copy()
        data['connected_habit'] = pleasant_habit.id
        response = self.client.post(
            '/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_DurationValidator(self):
        data = HABIT_DATA.copy()
        data['duration'] = 130
        response = self.client.post(
            '/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_ConnectedHabitValidator(self):
        data = HABIT_DATA.copy()
        non_pleasant_habit = Habit.objects.create(user=self.user, **data)

        data = HABIT_DATA.copy()
        del data['reward']
        data['connected_habit'] = non_pleasant_habit.id
        response = self.client.post(
            '/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_FrequencyValidator(self):
        data = HABIT_DATA.copy()
        data['frequency'] = 8
        response = self.client.post(
            '/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_PleasantRewardValidator(self):
        data = HABIT_DATA.copy()
        data['is_pleasant'] = True
        response = self.client.post(
            '/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


