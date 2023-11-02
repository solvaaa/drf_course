from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(10):
            user = User.objects.create(
                email=f'user{i}@mail.ru',
                first_name=f'Test{i}',
                last_name='Project',
                is_staff=False,
                is_superuser=False
            )

            user.set_password('11qwerty11')
            user.save()
