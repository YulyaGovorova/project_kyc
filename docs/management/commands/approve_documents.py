from django.core.management.base import BaseCommand
from docs.models import Document
from docs.utils import send_document_status_notification



class Command(BaseCommand):
    help = 'Approve documents and send notifications to users'

    def handle(self, *args, **options):
        documents_to_approve = Document.objects.filter(approved=False)

        for document in documents_to_approve:
            document.approve_document(document.user)
            send_document_status_notification(document, 'подтвержден')

        self.stdout.write(self.style.SUCCESS('Documents approved and notifications sent successfully'))
