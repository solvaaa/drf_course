from rest_framework import serializers

from habits.models import Habit
from habits.validators import \
    DurationValidator, \
    FrequencyValidator, \
    ConnectedHabitValidator, \
    RewardValidator, \
    PleasantRewardValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        exclude = ("periodic_task", )
        read_only_fields = ('user',)
        validators = [
            DurationValidator(field='duration'),
            FrequencyValidator(field='frequency'),
            ConnectedHabitValidator(field='connected_habit'),
            RewardValidator(field_1='connected_habit', field_2='reward'),
            PleasantRewardValidator(
                field_1='is_pleasant',
                field_2='connected_habit',
                field_3='reward'
            )
        ]
