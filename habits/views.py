from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitDetailView(RetrieveAPIView):
    """Shows details of the habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListView(ListAPIView):
    """Shows list of available habits"""
    serializer_class = HabitSerializer
    queryset =Habit.objects.all()


class HabitCreateView(CreateAPIView):
    """Creates new habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.owner = self.request.user
        obj.save()


class HabitUpdateView(UpdateAPIView):
    """Modifies habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyView(DestroyAPIView):
    """Deletes habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
