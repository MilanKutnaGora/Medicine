import random

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

random_code = str(random.randint(00000000, 99999999))


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=30, verbose_name='страна', **NULLABLE)
    verification_code = models.CharField(max_length=8, default=random_code,
                                         verbose_name='код подтверждения почты', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активность')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
