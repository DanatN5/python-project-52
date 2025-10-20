from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView

from task_manager.apps.task.filter import TaskFilter
from task_manager.apps.task.forms import TaskForm
from task_manager.apps.task.models import Task
from task_manager.mixins import AuthenticationMixin, AuthorRequiredMixin


class TasksView(FilterView, AuthenticationMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    def get_filterset(self, filterset_class):
        return filterset_class(self.request.GET,
                               queryset=self.get_queryset(),
                               request=self.request)


class TaskView(AuthenticationMixin, DetailView):
    model = Task
    template_name = 'task/task.html'
    context_object_name = 'task'


class CreateTask(AuthenticationMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'general/general_form.html'
    success_url = reverse_lazy('task_list')
    extra_context = {'title': 'Create task'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,
                         f'Task "{form.instance.name}" successfelly created!')
        return super().form_valid(form)


class UpdateTask(AuthenticationMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'general/general_form.html'
    success_url = reverse_lazy('task_list')
    extra_context = {'title': 'Update task'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,
                         f'Task "{form.instance.name}" successfelly updated!')
        return super().form_valid(form)


class DeleteTask(AuthorRequiredMixin, AuthenticationMixin,
                 SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'general/confirm_delete.html'
    success_url = reverse_lazy('task_list')
    success_message = 'Task successfully deleted'
    extra_context = {'title': 'Delete task'}
    context_object_name = 'object'