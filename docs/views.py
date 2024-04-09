from rest_framework import viewsets

from docs.models import Document
from docs.serializers import DocumentSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, FormParser)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()
        # Отправляем уведомление администратору
        send_notification_email.delay('admin@example.com', 'New document uploaded.')