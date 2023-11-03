from drf_yasg import openapi

HABIT_CREATE_CUSTOM_BODY = {
        'type': openapi.TYPE_OBJECT,
        'required': [
            'name',
            'place',
            'time',
            'action',
            'is_pleasant',
            'duration'
        ],
        'title': 'Habit',
        'properties': {
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                title='Название',
                maxLength=100),
            "place": openapi.Schema(
                type=openapi.TYPE_STRING,
                title='Место',
                maxLength=100),
            "time": openapi.Schema(
                type=openapi.TYPE_STRING,
                title='Время'),
            "action": openapi.Schema(
                type=openapi.TYPE_STRING,
                title='Время',
                maxLength=100),
            "is_pleasant": openapi.Schema(
                type=openapi.TYPE_BOOLEAN,
                title='Приятная?'),
            "frequency": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                title='Периодичность',
                minimum=1,
                maximum=7,
                default=1),
            "reward": openapi.Schema(
                type=openapi.TYPE_STRING,
                title='Вознаграждение',
                maxLength=100),
            "duration": openapi.Schema(
                type=openapi.TYPE_STRING,
                title='Продолжительность',
                minimum=1,
                maximum=120),
            "is_public": openapi.Schema(
                type=openapi.TYPE_BOOLEAN,
                title='Публичная?'),
            "connected_habit": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                title='Публичная?')
        }
}
