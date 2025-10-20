from django import forms

from task_manager.apps.label.models import Label


class LabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']
        labels = {
            'name': 'Имя',
        }