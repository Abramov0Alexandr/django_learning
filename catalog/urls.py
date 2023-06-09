from django.urls import path
from catalog.views import index, contacts, product_info, fashion_blog, blog_detail

urlpatterns = [
    path('', index, name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<slug:product_slug>/', product_info, name='product_info'),
    path('blog/', fashion_blog, name='blog'),
    path('blog/<slug:blog_slug>/', blog_detail, name='blog_detail'),
]
