from django.urls import reverse_lazy
from .models import Task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import TaskForm, TaskCreateForm


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('index')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_edit.html'
    # form_class = TaskForm
    success_url = reverse_lazy('index')
    fields = ['title', 'descript', 'deadline']


class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = TaskCreateForm
    success_url = reverse_lazy('index')


