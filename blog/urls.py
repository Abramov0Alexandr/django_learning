from django.urls import path
from blog import views


app_name = 'blog'


urlpatterns = [
    path('blog/', views.FashionBlogListView.as_view(), name='blog'),
    path('blog/<slug:blog_slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('create/', views.AddPostCreateView.as_view(),  name='blog_create'),
    path('edit/', views.DevelopingPostsListView.as_view(), name='developing_posts'),
    path('edit/release/<slug:blog_slug>/', views.ReleasePostUpdateView.as_view(), name='release_post'),
    path('blog/delete/<slug:blog_slug>', views.PostDeleteView.as_view(), name='post_delete'),

]
