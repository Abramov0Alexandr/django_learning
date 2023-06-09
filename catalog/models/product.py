from django.db import models
from django.urls import reverse_lazy
from slugify import slugify

from catalog.models.category import Category
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/catalog', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_change_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    in_stock = models.BooleanField(default=False, verbose_name='В продаже')

    product_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE
    )

    def __str__(self):
        return f"Наименование товара: {self.title}. " \
               f"Категория: {self.category}. " \
               f"Цена: {self.price}. " \
               f"Дата создания: {self.create_date}"

    def get_absolute_url(self):
        return reverse_lazy('catalog:product_info', kwargs={'product_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)

        permissions = [
            (
                'set_sales_status', 'Can change sales status'
            )
        ]
