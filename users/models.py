from django.contrib.auth.models import AbstractUser
from django.db import models
from blog.models.fashion_blog import NULLABLE


class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество', **NULLABLE)

    avatar = models.ImageField(upload_to='images/users', verbose_name='Автар', **NULLABLE)
    phone_number = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='Страна', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


