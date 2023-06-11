from django.shortcuts import render
from django.views import generic
from catalog.forms import CreatePostForm
from catalog.models import Product, FashionBlog


class IndexListView(generic.ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {'title': 'SkyStore', }


class ProductDetailView(generic.DetailView):

    model = Product
    template_name = 'catalog/product_detail.html'
    slug_url_kwarg = 'product_slug'

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['product_slug'])


def contacts(request):
    return render(request, 'catalog/contacts.html', {'title': 'Контакты'})


class FashionBlogListView(generic.ListView):
    model = FashionBlog
    template_name = 'catalog/blog.html'
    extra_context = {'title': 'SkyStore Blog'}

    def get_queryset(self):
        return FashionBlog.objects.filter(is_published=True)


class DevelopingPostsListView(generic.ListView):
    model = FashionBlog
    template_name = 'catalog/developing_posts.html'
    extra_context = {'title': 'В подготовке'}

    def get_queryset(self):
        return FashionBlog.objects.filter(is_published=False)


class BlogDetailView(generic.DetailView):

    model = FashionBlog
    template_name = 'catalog/blog_detail.html'
    slug_url_kwarg = 'blog_slug'

    def get_queryset(self):
        return FashionBlog.objects.filter(slug=self.kwargs['blog_slug'])

    def get_object(self, queryset=None):
        post = super().get_object()
        post.view_count += 1
        post.save()
        return post


class AddPostCreateView(generic.CreateView):
    form_class = CreatePostForm
    template_name = 'catalog/add_post.html'
    extra_context = {'title': 'Администрирование', }









