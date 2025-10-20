from django import forms
from django.contrib.auth.forms import AuthenticationForm

from task_manager.apps.users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=("Имя пользователя"),
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': ('Имя пользователя')}),
        required=True)
    password = forms.CharField(
        label=("Пароль"),
        min_length=4,
        widget=forms.PasswordInput(attrs={
            'placeholder': ('Пароль'),
            'autocomplete': 'current-password'}),
        required=True)

    class Meta:
        model = User
        fields = ['username', 'password']