import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, CommandError
from users.models import User

class Command(BaseCommand):
    """Создание superuser"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='from@example.com',
            username='Admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password(os.getenv('ADMIN_PASSWORD'))
        user.save()

