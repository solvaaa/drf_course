from rest_framework.serializers import ValidationError


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        dict_value = dict(value).get(self.field)
        if dict_value > 120:
            raise ValidationError('Время выполнения привычки должно быть '
                                  'не больше 120 секунд')
        elif dict_value <= 0:
            raise ValidationError('Неверное время выполнения привычки')

