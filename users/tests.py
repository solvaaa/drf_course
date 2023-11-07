from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


USER_DATA = {
    "email": "test@test.test",
    "password": "11qwerty11"
}


class UserTestCase(APITestCase):

    def test_register(self):
        data = USER_DATA.copy()
        response = self.client.post(
            '/user/register/',
            data=data
        )
        self.assertTrue(
            User.objects.all().exists()
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        user = User.objects.all().first()

        correct_response = {
            'id': user.id,
            'email': 'test@test.test',
            'first_name': '',
            'last_name': '',
            'telegram_handle': None,
            'subscribed_to_bot': False
        }
        self.assertEqual(
            response.json(),
            correct_response
        )

    def test_get_token(self):
        data = USER_DATA.copy()
        self.client.post(
            '/user/register/',
            data=data
        )
        response = self.client.post(
            '/user/token/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()), 2
        )
