from rest_framework.serializers import ValidationError


class DurationValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        dict_value = dict(value).get(self.field)
        if dict_value > 120:
            raise ValidationError('Слишком долгое время выполнения привычки')