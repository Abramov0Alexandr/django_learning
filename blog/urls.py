from django.urls import path
from blog.views import FashionBlogListView, BlogDetailView, \
    AddPostCreateView, DevelopingPostsListView, ReleasePostUpdateView


app_name = 'blog'


urlpatterns = [
    path('blog/', FashionBlogListView.as_view(), name='blog'),
    path('blog/<slug:blog_slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', AddPostCreateView.as_view(),  name='blog_create'),
    path('edit/', DevelopingPostsListView.as_view(), name='developing_posts'),
    path('edit/release/<slug:blog_slug>/', ReleasePostUpdateView.as_view(), name='release_post'),
]
