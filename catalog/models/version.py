from django.db import models


class Version(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version = models.IntegerField(verbose_name='Версия')
    version_title = models.CharField(max_length=250, verbose_name='Название версии')
    version_status = models.BooleanField(default=True, verbose_name='Признак активности')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('pk',)

    def __str__(self):
        return f"{self.version_title} {self.product}"
