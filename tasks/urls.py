from django.urls import path
from .views import TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView, TaskCreateView

urlpatterns = [
    path('task/create', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/edit', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('', TaskListView.as_view(), name='index'),
]