from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from task_manager.forms import LoginForm

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):

        return render(request, self.template_name)
    
class Login(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

def logout_view(request):
    logout(request)
    return redirect('login')


