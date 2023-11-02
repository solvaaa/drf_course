from rest_framework import serializers

from habits.models import Habit
from habits.validators import *


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ('user', )
        validators = [
            DurationValidator(field='duration'),
        ]
