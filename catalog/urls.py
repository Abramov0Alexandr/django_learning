from django.urls import path
from catalog.views import homepage, contacts, product_info


urlpatterns = [
    path('', homepage, name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_info, name='product_info')
]
