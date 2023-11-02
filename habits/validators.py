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


class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        dict_value = dict(value).get(self.field)
        if dict_value < 1 or dict_value > 7:
            raise ValidationError('Частота выполения привычки должна быть '
                                  'от 1 до 7 дней')