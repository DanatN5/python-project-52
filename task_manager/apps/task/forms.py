from django import forms

from task_manager.apps.task.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']
        widgets = {
            'label': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Имя',
            'status': 'Статус',
            'description': 'Описание',
            'executor': 'Исполнитель',
            'label': 'Метки',
        }