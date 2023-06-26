from django.urls import path
from blog import views


app_name = 'blog'


urlpatterns = [
    path('', views.FashionBlogListView.as_view(), name='blog'),
    path('developing_posts/', views.DevelopingPostsListView.as_view(), name='developing_posts'),
    path('create/', views.AddPostCreateView.as_view(), name='blog_create'),
    path('<slug:blog_slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('edite/<slug:blog_slug>/', views.ReleasePostUpdateView.as_view(), name='release_post'),
    path('developing_posts/delete/<slug:blog_slug>', views.PostDeleteView.as_view(), name='post_delete'),

]
