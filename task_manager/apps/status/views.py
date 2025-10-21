from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.apps.status.forms import StatusForm
from task_manager.apps.status.models import Status
from task_manager.mixins import AuthenticationMixin


class StatusesView(AuthenticationMixin, ListView):
    model = Status
    context_object_name = 'statuses'


class CreateStatus(AuthenticationMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'general/general_form.html'
    success_url = reverse_lazy('status_list')
    success_message = 'Статус успешно создан'
    extra_context = {'title': 'Создать статус',
                     'button': 'Создать'}


class UpdateStatus(AuthenticationMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'general/general_form.html'
    success_url = reverse_lazy('status_list')
    success_message = 'Статус успешно изменен'
    extra_context = {'title': 'Изменение статуса',
                     'button': 'Изменить'}


class DeleteStatus(AuthenticationMixin, DeleteView):
    model = Status
    template_name = 'general/confirm_delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('status_list')
    extra_context = {'title': 'Удаление статуса',
                     'button': 'Да, удалить'}
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request,
                             'Статус успешно удален')
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(self.request,
                    "Невозможно удалить статус, потому что он используется")
            return redirect(self.success_url)