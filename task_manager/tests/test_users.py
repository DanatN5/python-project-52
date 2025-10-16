from django.test import TestCase
from django.urls import reverse

from task_manager.apps.users.models import User


class UsersTests(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_signup_view(self):
        response = self.client.post(reverse('sign_up_user'), {
            "first_name": "Lord",
            "last_name": "Farquad",
            'username': 'LordFarquad',
            'password1': 'D5527gf74DbD!@',
            'password2': 'D5527gf74DbD!@',
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.last()
        self.assertEqual(user.first_name, 'Lord')
        self.assertEqual(user.last_name, 'Farquad')
        self.assertEqual(user.username, 'LordFarquad')

    def test_update_view(self):
        response = self.client.post(reverse('update_user', args=[self.user.pk]), {
            "first_name": self.user.first_name,
            "last_name": "Arthur",
            'username': 'King',
            'password1': 'D5527gf74DbD!@!!!',
            'password2': 'D5527gf74DbD!@!!!'
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.last_name, 'Arthur')

    def test_delete_view(self):
        response = self.client.post(reverse('delete_user', args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

