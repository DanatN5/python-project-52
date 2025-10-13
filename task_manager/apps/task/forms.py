from django import forms
from task_manager.apps.task.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'name', 'status', 'description', 'executor']