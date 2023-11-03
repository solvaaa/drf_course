from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.docs import HABIT_CREATE_CUSTOM_BODY
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
        **HABIT_CREATE_CUSTOM_BODY
    ))
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)


class HabitUpdateView(UpdateAPIView):
    """Modifies habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    @swagger_auto_schema(request_body=openapi.Schema(
        **HABIT_CREATE_CUSTOM_BODY
    ))
    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)

    @swagger_auto_schema(request_body=openapi.Schema(
        **HABIT_CREATE_CUSTOM_BODY
    ))
    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)


class HabitDestroyView(DestroyAPIView):
    """Deletes habit"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
