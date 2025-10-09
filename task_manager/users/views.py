from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from task_manager.users.models import User

# Create your views here.
class UsersView(ListView):
    model = User
    context_object_name = 'users'