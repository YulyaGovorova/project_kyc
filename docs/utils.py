
from notifications.signals import notify

from docs.models import CustomNotification



def send_document_status_notification(document, status):
    user = document.user
    message = f"Ваш документ '{document.title}' был {status}."
    actor = user  # Указываем отправителя уведомления
    notify.send(actor, recipient=user, verb=message, target=document)
    CustomNotification.objects.create(actor=actor, recipient=user, verb=message, target=document)


