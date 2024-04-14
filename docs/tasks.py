from celery import shared_task
from celery.exceptions import Retry
from django.core.mail import send_mail

# @shared_task
# def send_notification_email(recipient_email, message):
#     send_mail('Notification', message, 'from@example.com', [recipient_email])

@shared_task
def send_notification_email(recipient_email, message):
    try:
        send_mail('Notification', message, 'from@example.com', [recipient_email])
    except Exception as exc:
        raise Retry(exc)


