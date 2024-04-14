from django.db import models
from notifications.models import Notification

from users.models import User


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def approve_document(self, user):
        self.status = 'approved'
        self.save()
        DocumentStatusChange.objects.create(document=self, status='approved', changed_by=user)


class DocumentStatusChange(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.document.title} - {self.status}"

    class Meta:
        verbose_name = "Изменен статус документа"
        verbose_name_plural = "Изменены статусы документов"


class DocumentStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус документа"
        verbose_name_plural = "Статусы документов"


class CustomNotification(Notification):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return f'Уведомление для документа {self.document}'

    class Meta:
        verbose_name = "Пользовательское уведомление"
        verbose_name_plural = "Пользовательские уведомления"
