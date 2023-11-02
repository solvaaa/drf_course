from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import FivePagination
from habits.permissions import IsOwner, IsPublic
from habits.serializers import HabitSerializer


class HabitDetailView(RetrieveAPIView):
    """Shows details of the habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & (IsOwner | IsPublic)]


class HabitListView(ListAPIView):
    """Shows list of available habits"""
    serializer_class = HabitSerializer
    filter_backends = [OrderingFilter]
    ordering_fields =['id']
    pagination_class = FivePagination

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class PublicHabitListView(HabitListView):
    """Shows list of available habits"""
    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateView(CreateAPIView):
    """Creates new habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.user = self.request.user
        obj.save()


class HabitUpdateView(UpdateAPIView):
    """Modifies habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDestroyView(DestroyAPIView):
    """Deletes habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
