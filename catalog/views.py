from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render

from catalog.models import Product


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')


def homepage(request):
    context = {
        'title': 'SkyStore',
    }

    return render(request, 'catalog/homepage.html', context=context)


def contacts(request):
    return render(request, 'catalog/contacts.html', {'title': 'Контакты'})


def product_info(request, pk):

    info = Product.objects.filter(pk=pk)

    if len(info) == 0:
        raise Http404

    context = {
        'object_list': info,
    }
    return render(request, 'catalog/product_detail.html', context=context)
