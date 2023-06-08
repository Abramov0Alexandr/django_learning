from django.urls import path
from catalog.views import index, contacts, product_info, blog, fashion_blog

urlpatterns = [
    path('', index, name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('product/<slug:product_slug>/', product_info, name='product_info'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:blog_slug>/', fashion_blog, name='blog_info'),
]
