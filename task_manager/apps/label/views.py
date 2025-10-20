from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.apps.label.models import Label
from task_manager.mixins import AuthenticationMixin


class LabelView(AuthenticationMixin, ListView):
    model = Label
    context_object_name = 'labels'


class CreateLabel(AuthenticationMixin, SuccessMessageMixin, CreateView):
    model = Label
    template_name = 'general/general_form.html'
    fields = ['name']
    success_url = reverse_lazy('label_list')
    success_message = 'Label successfully created'
    extra_context = {'title': 'Create label'}


class UpdateLabel(AuthenticationMixin, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'general/general_form.html'
    fields = ['name']
    success_url = reverse_lazy('label_list')
    success_message = 'Label successfully updated'
    extra_context = {'title': 'Update label'}


class DeleteLabel(AuthenticationMixin, DeleteView):
    model = Label
    template_name = 'general/confirm_delete.html'
    context_object_name = 'label'
    success_url = reverse_lazy('label_list')
    extra_context = {'title': 'Delete label'}

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request,
                             f'Label {self.object.name} successfully deleted')
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request,
                           'You cannot delete this label. The label is in use')
        return redirect(self.success_url)
