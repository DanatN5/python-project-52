import django_filters
from django import forms

from task_manager.apps.labels.models import Label
from task_manager.apps.statuses.models import Status
from task_manager.apps.tasks.models import Task
from task_manager.apps.users.models import User


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label="Статус",
        empty_label="-----",
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label="Исполнитель",
        empty_label="-----",
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Метка",
        empty_label="-----",
    )

    self_tasks = django_filters.BooleanFilter(
        label="Только свои задачи",
        method="filter_self_tasks",
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'self_tasks']

    def filter_self_tasks(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(author=self.request.user)
        return queryset