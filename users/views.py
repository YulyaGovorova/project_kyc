
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
def upload_document(request):
    # Обработка загруженного документа
    # Отправка уведомления администратору
    send_mail('Новый документ', 'Поступил новый документ', 'govorovay15@gmail.com', ['tishyulya.1@yandex.ru'])

    return JsonResponse({'message': 'Документ успешно загружен'})