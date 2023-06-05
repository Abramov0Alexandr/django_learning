from django.db import models
from django.urls import reverse

from catalog.models.category import Category

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_change_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"Наименование товара: {self.title}. " \
               f"Категория: {self.category}. " \
               f"Цена: {self.price}. " \
               f"Дата создания: {self.create_date}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)
