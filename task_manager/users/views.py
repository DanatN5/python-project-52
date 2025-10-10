from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from task_manager.users.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class UsersView(ListView):
    model = User
    context_object_name = 'users'

class SignUpUser(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name']
    template_name = 'users/signup.html'
    success_url = reverse_lazy('user_list')

class UpdateUser(UpdateView):
    model = User
    fields = ['__all__']
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')

class DeleteUser(DeleteView):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')