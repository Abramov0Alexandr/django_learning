from django.db import models
from django.urls import reverse_lazy

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse_lazy('catalog:show_category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)
