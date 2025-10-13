from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView, ListView
from task_manager.apps.task.models import Task
from task_manager.apps.task.forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.apps.task.mixins import AuthorRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class TasksView(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskView(DetailView):
    model = Task
    template_name = 'task/task.html'
    context_object_name = 'task'

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,
                         f'Task "{form.instance.name}" successfelly created!')
        return super().form_valid(form)

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,
                         f'Task "{form.instance.name}" successfelly updated!')
        return super().form_valid(form)

class DeleteTask(AuthorRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task/confirm_delete.html'
    success_url = reverse_lazy('task_list')
    success_message = 'Task successfully deleted'