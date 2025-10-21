from django import forms

from task_manager.apps.status.models import Status


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['name']
        labels = {
            'name': 'Имя',
        }