from django.contrib.auth.forms import UserCreationForm

from task_manager.apps.users.models import User


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя',
        }
        help_texts = {
            'username': (
                'Обязательное поле. Не более 150 символов. '
                'Только буквы, цифры и символы @/./+/-/_.')
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = (
            'Ваш пароль должен содержать как минимум 3 символа.')
        self.fields['password2'].label = (
            'Подтверждение пароля')
        self.fields['password2'].help_text = (
            'Для подтверждения введите, пожалуйста, пароль ещё раз.')
        