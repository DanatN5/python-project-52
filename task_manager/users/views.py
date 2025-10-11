from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from task_manager.users.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class UsersView(ListView):
    model = User
    context_object_name = 'users'

class SignUpUser(CreateView):
    model = User
    fields = [ 'first_name', 'last_name', 'username', 'password']
    template_name = 'users/signup.html'
    success_url = reverse_lazy('user_list')

class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    fields = [ 'first_name', 'last_name', 'username', 'password']
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')

class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')