from django.http import Http404
from django.shortcuts import render
from catalog.models import Product, FashionBlog
from django.views import generic


class IndexListView(generic.ListView):
    model = Product
    template_name = 'catalog/index_list.html'
    extra_context = {'title': 'SkyStore', }


class ProductDetailView(generic.DetailView):

    model = Product
    template_name = 'catalog/product_detail.html'
    # slug_field = 'slug'
    slug_url_kwarg = 'product_slug'

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['product_slug'])


def contacts(request):
    return render(request, 'catalog/contacts.html', {'title': 'Контакты'})


class FashionBlogView(generic.ListView):
    model = FashionBlog
    template_name = 'catalog/blog.html'
    extra_context = {'title': 'SkyStore Blog'}


class BlogDetailView(generic.DetailView):

    model = FashionBlog
    template_name = 'catalog/blog_detail.html'
    slug_url_kwarg = 'blog_slug'

    def get_queryset(self):
        return FashionBlog.objects.filter(slug=self.kwargs['blog_slug'])
