from django.test import TestCase
from django.urls import reverse

from task_manager.apps.label.models import Label
from task_manager.apps.users.models import User


class LabelTests(TestCase):
    fixtures = ['label', 'users']

    def setUp(self):
        self.label = Label.objects.get(pk=2)

        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_create_label(self):
        response = self.client.post(reverse('create_label'), {
            "name": "Good",
        })
        self.assertEqual(response.status_code, 302)
        label = Label.objects.last()
        self.assertEqual(label.name, 'Good')
 
    def test_update_label(self):
        response = self.client.post(
            reverse('update_label', args=[self.label.pk]), {
            "name": "Label5",
        })
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Label5')

    def test_delete_label(self):
        response = self.client.post(
            reverse('delete_label', args=[self.label.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(pk=self.label.pk).exists())
