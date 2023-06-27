from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from blog.forms import CreatePostForm
from blog.models import FashionBlog


class FashionBlogListView(generic.ListView):
    queryset = FashionBlog.objects.filter(is_published=True)
    template_name = 'blog/blog.html'
    extra_context = {'title': 'SkyStore Blog'}


class DevelopingPostsListView(generic.ListView):
    queryset = FashionBlog.objects.filter(is_published=False)
    template_name = 'blog/developing_posts.html'
    extra_context = {'title': 'В подготовке'}


class BlogDetailView(generic.DetailView):

    model = FashionBlog
    template_name = 'blog/blog_detail.html'
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
    template_name = 'blog/add_post.html'
    extra_context = {'title': 'Администрирование', }


class ReleasePostUpdateView(generic.UpdateView):
    model = FashionBlog
    form_class = CreatePostForm
    template_name = 'blog/add_post.html'
    extra_context = {'title': 'Администрирование', }
    slug_url_kwarg = 'blog_slug'

    def get_queryset(self):
        return FashionBlog.objects.filter(slug=self.kwargs['blog_slug'])


class PostDeleteView(generic.DeleteView):
    model = FashionBlog
    template_name = 'blog/deleting_confirm.html'
    slug_url_kwarg = 'blog_slug'
    success_url = reverse_lazy('blog:developing_posts')

    def get_queryset(self):
        return FashionBlog.objects.filter(slug=self.kwargs['blog_slug'])


def toggle_published_status(request, blog_slug):
    post = get_object_or_404(FashionBlog, slug=blog_slug)

    if post.is_published:
        post.is_published = False
    else:
        post.is_published = True

    post.save()

    return redirect(reverse('blog:developing_posts'))
