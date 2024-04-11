from django.core.management.base import BaseCommand
from docs.tasks import send_notification_email

from docs.models import Document
from docs.utils import send_document_status_notification


# class Command(BaseCommand):
#     help = 'Approve documents and send notifications to users'
#
#     def handle(self, *args, **options):
#         documents_to_approve = Document.objects.filter(approved=False)
#
#         for document in documents_to_approve:
#             # Подтверждение документа
#             document.approved = True
#             document.save()
#             # Отправляем уведомление пользователю
#             send_notification_email.delay(document.user.email, document.title)
#
#         self.stdout.write(self.style.SUCCESS('Documents approved and notifications sent successfully'))

class Command(BaseCommand):
    help = 'Approve documents and send notifications to users'

    def handle(self, *args, **options):
        documents_to_approve = Document.objects.filter(approved=False)

        for document in documents_to_approve:
            document.approve_document(document.user)
            send_document_status_notification(document, 'approved')

        self.stdout.write(self.style.SUCCESS('Documents approved and notifications sent successfully'))