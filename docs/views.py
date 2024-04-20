from rest_framework import viewsets, status
from rest_framework.response import Response

from docs.models import Document
from docs.serializers import DocumentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from docs.tasks import send_notification_email


class DocumentViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с документами,
    CRUD операции над документами.
    Отправляет уведомления пользователю
    о статусе его документа.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        print('Received request to create a new document')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        instance = serializer.save()
        print(f'New document created: {instance.title}')

        send_notification_email.delay('admin@example.com', f'New document uploaded: {instance.title}')