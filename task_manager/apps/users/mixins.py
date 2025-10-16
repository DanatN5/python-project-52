from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class AuthorizationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kweargs):
        obj = self.get_object()
        if obj != request.user:
            messages.error(self.request, 'You cannot change other user profiles')
            return redirect('user_list')
        return super().dispatch(request, *args, **kweargs)