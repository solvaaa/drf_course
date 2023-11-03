from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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
    """Shows list of available public habits"""
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

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name', 'place', 'time', 'action', 'is_pleasant', 'duration'],
        title='Habit',
        properties={
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
                title='Публичная?'),
    }))
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)


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
