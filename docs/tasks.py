from celery import shared_task
from celery.exceptions import Retry
from django.core.mail import send_mail


@shared_task
def send_notification_email(recipient_email, message): # Задача Celery для отправки электронной почты с уведомлением, подтверждением.
    try:
        send_mail('Notification', message, 'govorovay15@gmail.com', ['tishyulya.1@yandex.ru'])
    except Exception as exc:
        raise Retry(exc)


