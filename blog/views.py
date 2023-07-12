from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from blog.forms import CreatePostForm
from blog.models import FashionBlog


class FashionBlogListView(generic.ListView):
    queryset = FashionBlog.objects.filter(is_published=True)
    template_name = 'blog/blog.html'


class DevelopingPostsListView(LoginRequiredMixin, generic.ListView):
    queryset = FashionBlog.objects.filter(is_published=False)
    template_name = 'blog/developing_posts.html'


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


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'blog.add_fashionblog'
    form_class = CreatePostForm
    template_name = 'blog/add_post.html'


class ReleasePostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = FashionBlog
    form_class = CreatePostForm
    template_name = 'blog/add_post.html'
    slug_url_kwarg = 'blog_slug'

    def get_queryset(self):
        return FashionBlog.objects.filter(slug=self.kwargs['blog_slug'])


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = FashionBlog
    template_name = 'blog/confirm_delete_blog.html'
    slug_url_kwarg = 'blog_slug'
    success_url = reverse_lazy('blog:developing_posts')

    def get_queryset(self):
        return FashionBlog.objects.filter(slug=self.kwargs['blog_slug'])


class TogglePublishedStatusView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'blog.change_fashionblog'

    def get(self, request, blog_slug):
        post = get_object_or_404(FashionBlog, slug=blog_slug)

        if post.is_published:
            post.is_published = False
        else:
            post.is_published = True

        post.save()

        if post.is_published:
            return redirect(reverse('blog:blog'))
        else:
            return redirect(reverse('blog:developing_posts'))
