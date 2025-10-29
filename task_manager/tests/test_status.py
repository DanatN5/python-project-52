import pytest
from django.test import TestCase
from django.urls import reverse

from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User


@pytest.mark.django_db
class StatusTests(TestCase):
    fixtures = ['status', 'users']

    def setUp(self):
        self.status = Status.objects.get(pk=2)

        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_create_status(self):
        response = self.client.post(reverse('create_status'), {
            "name": "Good",
        })
        self.assertEqual(response.status_code, 302)
        status = Status.objects.last()
        self.assertEqual(status.name, 'Good')
 
    def test_update_status(self):
        response = self.client.post(
            reverse('update_status', args=[self.status.pk]), {
            "name": "Niceee",
        })
        self.assertEqual(response.status_code, 302)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Niceee')

    def test_delete_status(self):
        response = self.client.post(
            reverse('delete_status', args=[self.status.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
