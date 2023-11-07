from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    telegram_handle = models.CharField(
        max_length=100,
        verbose_name='Telegram',
        unique=True, **NULLABLE)
    chat_id = models.CharField(max_length=100,
                               verbose_name='id чата в Телеграме',
                               **NULLABLE)
    subscribed_to_bot = models.BooleanField(default=False,
                                            verbose_name='подписан на бота?')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
