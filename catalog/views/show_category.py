from django.shortcuts import render
from catalog.models import Product, Category


def show_category(request, cat_id):
    product = Product.objects.filter(category_id=cat_id)
    cats = Category.objects.all()

    context = {
        'product': product,
        'cats': cats,
        'cat_selected': cat_id,
    }

    return render(request, 'catalog/index.html', context=context)
