from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        man_clothes = Category.objects.get(title='Мужская одежда')
        women_clothes = Category.objects.get(title='Женская одежда')
        accessories = Category.objects.get(title='Аксессуары')

        products_list = [
            {'title': 'Зимняя куртка', 'description': 'Зимняя утепленная мужская куртка',
             'category': man_clothes, 'price': 14000.0},
            {'title': 'Платье', 'description': 'Летнее платье',
             'category': women_clothes, 'price': 4200.0},
            {'title': 'Наручные часы', 'description': 'Механические мужские часы',
             'category': accessories, 'price': 23000.0}
        ]

        Product.objects.all().delete()

        products_for_create = []

        for product in products_list:
            products_for_create.append(
                Product(**product)
            )

        Product.objects.bulk_create(products_for_create)
