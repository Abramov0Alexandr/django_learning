from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """наименование,
    описание."""
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')


class Product(models.Model):

    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Цена')
    create_date = models.DateTimeField(verbose_name='Дата создания')
    last_change_date = models.DateTimeField(verbose_name='Дата последнего изменения')
