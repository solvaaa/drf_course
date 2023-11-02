from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitDetailView(RetrieveAPIView):
    """Shows details of the habit"""
    queryset = Habit.objects.all().order_by('id')
    serializer_class = HabitSerializer


class HabitListView(ListAPIView):
    """Shows list of available habits"""
    serializer_class = HabitSerializer
    queryset =Habit.objects.all()

    filter_backends = [OrderingFilter]
    ordering_fields =['id']


class HabitCreateView(CreateAPIView):
    """Creates new habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.user = self.request.user
        obj.save()


class HabitUpdateView(UpdateAPIView):
    """Modifies habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyView(DestroyAPIView):
    """Deletes habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
