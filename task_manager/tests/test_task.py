import pytest
from django.test import TestCase
from django.urls import reverse

from task_manager.apps.tasks.models import Task
from task_manager.apps.users.models import User


@pytest.mark.django_db
class LabelTests(TestCase):
    fixtures = ['task', 'users', 'label', 'status']

    def setUp(self):
        self.task = Task.objects.get(pk=1)

        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_task_list(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)

    def test_task(self):
        response = self.client.get(reverse('task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)
        self.assertEqual(self.task.name, 'Task55')
        self.assertEqual(self.task.status.name, 'splitty')

    def test_task_create(self):
        response = self.client.post(reverse('create_task'), {
            'name': 'New task',
            'description': 'New description',
            'status': self.task.status.id,
            'executor': self.task.executor.id,
            'labels': [2, 3],
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='New task').exists())

    def test_task_update(self):
        response = self.client.post(
            reverse('update_task', args=[self.task.id]), {
            'name': 'Updated task',
            'description': 'Updated description',
            'status': self.task.status.id,
            'executor': self.task.executor.id,
            'labels': [2],
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated task')

    def test_task_delete(self):
        response = self.client.post(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(name=self.task.name).exists())

    def test_task_delete_forbidden(self):
        task = Task.objects.get(pk=3)
        response = self.client.post(reverse('delete_task', args=[task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name=task.name).exists())