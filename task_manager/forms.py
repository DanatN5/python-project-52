from django.contrib.auth.forms import AuthenticationForm
from django import forms
from task_manager.apps.users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=("Username"),
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': ('Username')}),
        required=True)
    password = forms.CharField(
        label=("Password"),
        min_length=4,
        widget=forms.PasswordInput(attrs={
            'placeholder': ('Password'),
            'autocomplete': 'current-password'}),
        required=True)

    class Meta:
        model = User
        fields = ['username', 'password']