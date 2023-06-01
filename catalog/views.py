from django.shortcuts import render

from catalog.models import Product


def homepage(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'SkyStore'
    }

    return render(request, 'catalog/homepage.html', context=context)


def contacts(request):
    return render(request, 'catalog/contacts.html', {'title': 'Контакты'})


def product_info(request, pk):
    context = {
        'object_list': Product.objects.filter(pk=pk),
    }
    return render(request, 'catalog/product_detail.html', context=context)
