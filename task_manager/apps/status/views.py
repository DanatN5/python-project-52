from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.apps.status.models import Status


class StatusesView(ListView):
    model = Status
    context_object_name = 'statuses'


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'status/status_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list')
    success_message = 'Status successfully created'


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'status/status_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list')
    success_message = 'Status successfully updated'


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'status/confirm_delete.html'
    context_object_name = 'status'
    success_url = reverse_lazy('status_list')