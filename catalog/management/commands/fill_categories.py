from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        category_list = [
            {'title': 'Мужская одежда', 'description': 'Всесезонная мужская одежда'},
            {'title': 'Женская одежда', 'description': 'Всесезонная женская одежда'},
            {'title': 'Аксессуары', 'description': 'Мужские и женские аксессуары'}
        ]

        Category.objects.all().delete()

        categories_for_create = []

        for categories in category_list:
            categories_for_create.append(
                Category(**categories)
            )

        Category.objects.bulk_create(categories_for_create)
