from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Task
from datetime import datetime

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descript', 'deadline']


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descript', 'author', 'task_created_date','deadline']
        widgets = {
            'title' : TextInput(attrs={'placeholder':"title"}),
            'descript': Textarea(),
            'task_created_date': DateTimeInput(attrs={'placeholder':"YYYY-MM-DD HH:MM:SS"}),
            'deadline': DateTimeInput(attrs={'placeholder':"YYYY-MM-DDx HH:MM:SS"}),
        }