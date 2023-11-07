from rest_framework.serializers import ValidationError


class DurationValidator:
    '''Checks if duration of a habit is between 1 and 120 seconds'''
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
    '''Checks if frequenecy of a habit is between 1 and 7 days'''
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        frequency = dict(value).get(self.field)
        if frequency < 1 or frequency > 7:
            raise ValidationError('Частота выполения привычки должна быть '
                                  'от 1 до 7 дней')


class ConnectedHabitValidator:
    '''Checks if connected habit is a pleasant habit'''
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        connected_habit = dict(value).get(self.field)
        if connected_habit is not None:
            if not connected_habit.is_pleasant:
                raise ValidationError('Связанная привычка должна быть '
                                      'приятной привычкой')


class RewardValidator:
    '''Checks if there is only one reward or connected habit as a reward'''
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        connected_habit = dict(value).get(self.field_1)
        reward = dict(value).get(self.field_2)
        if reward is not None and connected_habit is not None:
            raise ValidationError('Поля "Вознаграждение" и '
                                  '"Связанная привычка"'
                                  'нельзя использовать одновременно')


class PleasantRewardValidator:
    '''Checks if pleasant habit doesn't have a reward'''
    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        is_pleasant = dict(value).get(self.field_1)
        connected_habit = dict(value).get(self.field_2)
        reward = dict(value).get(self.field_3)
        if is_pleasant:
            if reward is not None or connected_habit is not None:
                raise ValidationError('У приятной привычки не может быть '
                                      'вознаграждения')
