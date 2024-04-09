from django.contrib import admin
from docs.models import Document, DocumentStatus
from docs.utils import send_document_status_notification

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status']
    actions = ['confirm_documents', 'reject_documents']

    def confirm_documents(self, request, queryset):
        queryset.update(status=DocumentStatus.objects.get(name='Подтвержден'))
    # confirm_documents.short_cdescription = "Подтвердить выбранные документы"
        for document in queryset:
            send_document_status_notification.delay(document.id, 'подтвержден')

    def reject_documents(self, request, queryset):
        queryset.update(status=DocumentStatus.objects.get(name='Отклонен'))
    # reject_documents.short_description = "Отклонить выбранные документы"
        for document in queryset:
            send_document_status_notification.delay(document.id, 'отклонен')

admin.site.register(DocumentStatus)