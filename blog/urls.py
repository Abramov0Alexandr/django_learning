from django.urls import path
from django.views.decorators.cache import cache_page
from blog import views


app_name = 'blog'


urlpatterns = [
    path('', cache_page(60)(views.FashionBlogListView.as_view()), name='blog'),
    path('developing_posts/', views.DevelopingPostsListView.as_view(), name='developing_posts'),
    path('create/', views.PostCreateView.as_view(), name='blog_create'),
    path('<slug:blog_slug>/', cache_page(60)(views.BlogDetailView.as_view()), name='blog_detail'),
    path('edite/<slug:blog_slug>/', views.ReleasePostUpdateView.as_view(), name='release_post'),
    path('developing_posts/delete/<slug:blog_slug>', views.PostDeleteView.as_view(), name='post_delete'),
    path('activity/<slug:blog_slug>', views.TogglePublishedStatusView.as_view(), name='toggle_published_status'),
]
