import os

from django.test import TestCase
from django.core import mail
from django.core.management import call_command
from django.contrib.auth import get_user_model
from users.models import User
from users.views import upload_document

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(email='test@example.com', username='TestUser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'TestUser')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_upload_document_view(self):
        request = self.client.post('/upload_document/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Новый документ')
        self.assertEqual(mail.outbox[0].body, 'Поступил новый документ')


