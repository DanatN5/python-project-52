from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class AuthenticationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                messages.error(self.request, ("Вы не залогинены"))
            )
            return redirect(reverse_lazy("login"))
        return super(
            LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class AuthorizationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kweargs):
        obj = self.get_object()
        if obj != request.user:
            messages.error(self.request,
                           'У вас не прав для изменения другого пользователя')
            return redirect(reverse_lazy('user_list'))
        return super().dispatch(request, *args, **kweargs)
    

class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user
    
    def handle_no_permission(self):
        messages.error(self.request, 'Задачу может удалить только ее автор')
        return redirect(reverse_lazy('task_list'))