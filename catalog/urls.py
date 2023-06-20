from django.urls import path
from catalog.views import IndexListView, contacts, \
    ProductDetailView, FashionBlogListView, BlogDetailView, \
    AddPostCreateView, DevelopingPostsListView


urlpatterns = [
    path('', IndexListView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<slug:product_slug>/', ProductDetailView.as_view(), name='product_info'),
    path('blog/', FashionBlogListView.as_view(), name='blog'),
    path('blog/<slug:blog_slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', AddPostCreateView.as_view(),  name='blog_create'),
    path('edit/', DevelopingPostsListView.as_view(), name='developing_posts'),

]
