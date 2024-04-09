


from notifications.signals import notify

def send_document_status_notification(document, status):
    user = document.user
    message = f"Ваш документ '{document.title}' был {status}."
    notify.send(sender=None, recipient=user, verb=message, target=document)