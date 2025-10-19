from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


class AuthenticationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                messages.error(self.request, ("You are not authenticated."))
            )
            return redirect(reverse_lazy("login"))
        return super(
            LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class AuthorizationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kweargs):
        obj = self.get_object()
        if obj != request.user:
            messages.error(self.request, 'You cannot change other user profiles')
            return redirect(reverse_lazy('user_list'))
        return super().dispatch(request, *args, **kweargs)
    
class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user
    
    def handle_no_permission(self):
        messages.error(self.request, 'Only task author can delete this task')
        return redirect(reverse_lazy('task_list'))