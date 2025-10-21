from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from task_manager.forms import LoginForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):

        return render(request, self.template_name)
    

class Login(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    success_message = 'Вы залогинены'


def logout_view(request):
    messages.info(request,
                'Вы разлогинены')
    logout(request)
    return redirect('/')


