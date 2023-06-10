from django.http import Http404
from django.shortcuts import render
from catalog.models import Product, FashionBlog
from django.views import generic


class IndexListView(generic.ListView):
    model = Product
    template_name = 'catalog/index.html'
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

    def get_queryset(self):
        return FashionBlog.objects.filter(is_published=True)


class BlogDetailView(generic.DetailView):

    model = FashionBlog
    template_name = 'catalog/blog_detail.html'
    slug_url_kwarg = 'blog_slug'

    def get_queryset(self):
        return FashionBlog.objects.filter(slug=self.kwargs['blog_slug'])


class BlogCreateView(generic.CreateView):
    model = FashionBlog
    fields = ('title', 'content', 'image', )
    template_name = 'catalog/add_post.html'





