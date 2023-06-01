from django import template

register = template.Library()


@register.filter()
def app_media(val):
    if val:
        return f'/media/{val}'

    return '/static/coming_soon.jpg'
