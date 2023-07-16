from django.shortcuts import render
from catalog.models import Product, Category
from catalog.services import get_category_cache


def show_category(request, cat_id):
    product = Product.objects.filter(category_id=cat_id)
    cats = get_category_cache()

    context = {
        'product': product,
        'cats': cats,
        'cat_selected': cat_id,
    }

    return render(request, 'catalog/index.html', context=context)
