from django.db import models
from django.urls import reverse_lazy
from slugify import slugify


NULLABLE = {'blank': True, 'null': True}


class FashionBlog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    image = models.ImageField(upload_to='images/blog', verbose_name='Превью', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Заголовок: {self.title}"

    def get_absolute_url(self):
        return reverse_lazy('catalog:blog_detail', kwargs={'blog_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ('pk',)
