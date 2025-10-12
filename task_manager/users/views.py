from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from task_manager.users.models import User
from task_manager.users.forms import UserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.users.mixins import AuthorizationMixin

# Create your views here.
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