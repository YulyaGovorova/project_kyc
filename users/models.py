from django.contrib.auth.models import AbstractUser
from django.db import models

from docs.utils import NULLABLE


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='username', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
