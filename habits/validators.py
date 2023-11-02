from rest_framework.serializers import ValidationError


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)
        if duration > 120:
            raise ValidationError('Время выполнения привычки должно быть '
                                  'не больше 120 секунд')
        elif duration <= 0:
            raise ValidationError('Неверное время выполнения привычки')


class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        frequency = dict(value).get(self.field)
        if frequency < 1 or frequency > 7:
            raise ValidationError('Частота выполения привычки должна быть '
                                  'от 1 до 7 дней')


class ConnectedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        connected_habit = dict(value).get(self.field)
        if connected_habit is not None:
            if not connected_habit.is_pleasant:
                raise ValidationError('Связанная привычка должна быть '
                                      'приятной привычкой')
