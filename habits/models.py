from django.db import models

from users.models import NULLABLE, User


# Create your models here.
class Habit(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='пользователь', null=True)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='приятная?')
    connected_habit = models.ForeignKey('self', on_delete=models.SET_NULL,
                                        verbose_name='связанная привычка',
                                        **NULLABLE)
    frequency = models.PositiveSmallIntegerField(verbose_name='периодичность',
                                                 default=1)
    reward = models.CharField(max_length=100, verbose_name='вознаграждение',
                              **NULLABLE)
    duration = models.PositiveSmallIntegerField(verbose_name='продолжительность')
    is_public = models.BooleanField(default=False, verbose_name='публичная?')

    def __str__(self):
        return f'{self.name}, {self.user}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

