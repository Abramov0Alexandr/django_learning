from django.http import Http404
from django.shortcuts import render
from catalog.models import Product, FashionBlog


def index(request):
    context = {
        'title': 'SkyStore',
    }

    return render(request, 'catalog/index.html', context=context)


def contacts(request):
    return render(request, 'catalog/contacts.html', {'title': 'Контакты'})


def product_info(request, product_slug):

    info = Product.objects.filter(slug=product_slug)

    if len(info) == 0:
        raise Http404

    context = {
        'object_list': info,
    }
    return render(request, 'catalog/product_detail.html', context=context)


def blog(request):
    return render(request, 'catalog/blog.html', {'title': 'SkyStore Blog'})


def fashion_blog(request, blog_slug):
    context = {
        'object_list': FashionBlog.objects.filter(slug=blog_slug),
    }

    return render(request, 'catalog/blog_detail.html', context=context)
