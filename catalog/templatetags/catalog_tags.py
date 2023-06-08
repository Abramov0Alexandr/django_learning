from django import template
from catalog.models import Product, FashionBlog


register = template.Library()


@register.filter()
def upload_media(image):
    if image:
        return f'/media/{image}'

    return '/static/coming_soon.jpg'


@register.simple_tag()
def get_products():
    return Product.objects.all()


@register.simple_tag()
def get_blog_post():
    return FashionBlog.objects.all()
