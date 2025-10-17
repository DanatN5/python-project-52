from django.urls import reverse_lazy
from django.views.generic import ListView
from task_manager.apps.status.models import Status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError


class StatusesView(ListView):
    model = Status
    context_object_name = 'statuses'

class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'general/general_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list')
    success_message = 'Status successfully created'
    extra_context = {'title': 'Create status'}

class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'general/general_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list')
    success_message = 'Status successfully updated'
    extra_context = {'title': 'Update status'}

class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'general/confirm_delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('status_list')
    extra_context = {'title': 'Delete status'}
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, f'Status {self.object.name} successfully deleted')
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(self.request, 'You cannot delete this status. The status is in use')
            return redirect(self.success_url)