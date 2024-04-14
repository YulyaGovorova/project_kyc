from django.contrib import admin
from docs.models import Document, DocumentStatus
from docs.utils import send_document_status_notification

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status']
    actions = ['confirm_documents', 'reject_documents']

    def confirm_documents(self, request, queryset):
        confirmed_status = DocumentStatus.objects.get(name='Подтвержден')
        queryset.update(status=confirmed_status)
        for document in queryset:
            send_document_status_notification.delay(document, confirmed_status)

    def reject_documents(self, request, queryset):
        rejected_status = DocumentStatus.objects.get(name='Отклонен')
        queryset.update(status=rejected_status)
        for document in queryset:
            send_document_status_notification.delay(document, rejected_status)