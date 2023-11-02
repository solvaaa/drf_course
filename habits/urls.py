from django.urls import path

from habits.apps import HabitsConfig
from habits.views import *

appname = HabitsConfig.name

url_patterns = [
    path('/', HabitListView.as_view(), name='lesson_list'),
    path('<int:pk>', HabitDetailView.as_view(), name='lesson_detail'),
    path('create/', HabitCreateView.as_view(), name='lesson_create'),
    path('edit/<int:pk>', HabitUpdateView.as_view(), name='lesson_edit'),
    path('delete/<int:pk>', HabitDestroyView.as_view(), name='lesson_delete'),
]