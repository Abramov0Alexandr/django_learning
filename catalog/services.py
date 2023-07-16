from django.core.cache import cache
from catalog.models import Category
from config import settings


def get_category_cache():
    if settings.CACHE_ENABLED:
        key = 'catalogs_list'
        catalogs_list = cache
        if catalogs_list is None:
            catalogs_list = Category.objects.all()
            cache.set(key, catalogs_list)
    else:
        catalogs_list = Category.objects.all()

    return catalogs_list
