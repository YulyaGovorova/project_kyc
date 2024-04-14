import unittest

from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from docs.models import Document, DocumentStatusChange
from docs.tasks import send_notification_email

from users.models import User


class DocumentModelTestCase(TestCase):
    def test_approve_document(self):
        user = User.objects.create(email='test@example.com')
        document = Document.objects.create(title='Test Document', user=user, status='pending')

        document.approve_document(user)

        self.assertEqual(document.status, 'approved')
        self.assertTrue(
            DocumentStatusChange.objects.filter(document=document, status='approved', changed_by=user).exists())

    def test_send_notification_email(self):
        recipient_email = 'test@example.com'
        message = 'Test message'

        send_notification_email(recipient_email, message)

        # Добавьте здесь проверки для убедительности

class DocumentViewSetTestCase(TestCase):
    def test_create_document(self):
        client = APIClient()
        url = reverse('document-list')

        # Создаем временный файл для тестирования
        test_file = SimpleUploadedFile("test.pdf", b"file_content", content_type="application/pdf")

        data = {'title': 'Test Document', 'file': test_file,
                'user': 1}  # Предполагается, что пользователь с id=1 существует

        response = client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()



