from django import forms

from task_manager.apps.task.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']
        labels = {
            'name': 'Имя',
            'status': 'Статус',
            'description': 'Описание',
            'executor': 'Исполнитель',
            'label': 'Метки',
        }