from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

class AuthorizationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kweargs):
        obj = self.get_object()
        if obj != request.user:
            return HttpResponseForbidden("You cannot change other user profiles")
        return super().dispatch(request, *args, **kweargs)