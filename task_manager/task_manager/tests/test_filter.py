from django.test import TestCase
from django.urls import reverse

from task_manager.apps.label.models import Label
from task_manager.apps.status.models import Status
from task_manager.apps.task.models import Task
from task_manager.apps.users.models import User


class FilterTests(TestCase):
    fixtures = ['task', 'users', 'label', 'status']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_access(self):
        self.client.post(reverse('logout'))
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 302)

    def test_filter_by_status(self):
        status = Status.objects.get(pk=1)
        task_expected = Task.objects.get(pk=4)
        task_unexpected = Task.objects.get(pk=1)
        response = self.client.get(reverse('task_list'), {
            'status': status.id,
        })
        self.assertEqual(response.status_code, 200)
        tasks = list(response.context['tasks'])
        self.assertIn(task_expected, tasks)
        self.assertNotIn(task_unexpected, tasks)

    def test_filter_by_label(self):
        label = Label.objects.get(pk=1)
        task_expected = Task.objects.get(pk=2)
        task_unexpected = Task.objects.get(pk=1)
        response = self.client.get(reverse('task_list'), {
            'label': label.id,
        })
        self.assertEqual(response.status_code, 200)
        tasks = list(response.context['tasks'])
        self.assertIn(task_expected, tasks)
        self.assertNotIn(task_unexpected, tasks)

    def test_filter_by_executor(self):
        executor = User.objects.get(pk=1)
        task_expected = Task.objects.get(pk=2)
        task_unexpected = Task.objects.get(pk=1)
        response = self.client.get(reverse('task_list'), {
            'executor': executor.id,
        })
        self.assertEqual(response.status_code, 200)
        tasks = list(response.context['tasks'])
        self.assertIn(task_expected, tasks)
        self.assertNotIn(task_unexpected, tasks)

    def test_filter_combined(self):
        executor = User.objects.get(pk=1)
        label = Label.objects.get(pk=1)
        status = Status.objects.get(pk=3)
        task_expected = Task.objects.get(pk=2)
        task_unexpected = Task.objects.get(pk=3)
        response = self.client.get(reverse('task_list'), {
            'executor': executor.id,
            'label': label.id,
            'status': status.id,
        })
        self.assertEqual(response.status_code, 200)
        tasks = list(response.context['tasks'])
        self.assertIn(task_expected, tasks)
        self.assertNotIn(task_unexpected, tasks)