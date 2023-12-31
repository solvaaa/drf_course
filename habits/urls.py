from django.urls import path

from habits.apps import HabitsConfig
from habits.views import \
    HabitListView, \
    PublicHabitListView, \
    HabitDetailView, \
    HabitCreateView, \
    HabitUpdateView, \
    HabitDestroyView

appname = HabitsConfig.name

urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),
    path('public/', PublicHabitListView.as_view(), name='public_list'),
    path('<int:pk>', HabitDetailView.as_view(), name='habit_detail'),
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('edit/<int:pk>', HabitUpdateView.as_view(), name='habit_edit'),
    path('delete/<int:pk>', HabitDestroyView.as_view(), name='habit_delete'),
]
