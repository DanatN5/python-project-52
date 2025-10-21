from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.apps.users.forms import UserForm
from task_manager.apps.users.models import User
from task_manager.mixins import AuthorizationMixin


class UsersView(ListView):
    model = User
    context_object_name = 'users'


class SignUpUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'general/general_form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация',
        'button': 'Зарегистрировать',
        }
    success_message = 'Пользователь успешно зарегистрирован'


class UpdateUser(SuccessMessageMixin, AuthorizationMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'general/general_form.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')
    success_message = 'Пользователь успешно изменен'
    extra_context = {
        'title': 'Изменение пользователя',
        'button': 'Изменить',
        }


class DeleteUser(SuccessMessageMixin, AuthorizationMixin, DeleteView):
    model = User
    template_name = 'general/confirm_delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('user_list')
    success_message = 'Пользователь успешно удален'
    extra_context = {
        'title': 'Удаление пользователя',
        'button': 'Да, удалить',
        }
    