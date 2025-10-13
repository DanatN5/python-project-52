from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.apps.users.forms import UserForm
from task_manager.apps.users.mixins import AuthorizationMixin
from task_manager.apps.users.models import User


class UsersView(ListView):
    model = User
    context_object_name = 'users'


class SignUpUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


class UpdateUser(AuthorizationMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')


class DeleteUser(AuthorizationMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')