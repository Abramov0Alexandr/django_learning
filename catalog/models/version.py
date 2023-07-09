from django.db import models
from django.core.exceptions import ValidationError


class Version(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='version', verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Версия')
    version_title = models.CharField(max_length=250, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак активности')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('pk',)

    def __str__(self):
        return f"{self.version_title} {self.product}"

    def clean(self) -> None:

        super().clean()
        if Version.objects.filter(
                product=self.product,
                is_active=True
        ).exists():
            raise ValidationError('Вы можете установить только одну активную версию')
