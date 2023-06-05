from django import template
from catalog.models import Product


register = template.Library()


@register.filter()
def upload_media(image):
    if image:
        return f'/media/{image}'

    return '/static/coming_soon.jpg'


@register.simple_tag()
def get_products():
    return Product.objects.all()



