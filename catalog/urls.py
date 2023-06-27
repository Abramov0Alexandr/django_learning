from django.urls import path
from catalog.views import IndexListView, ContactsView, ProductDetailView, CreateProductCreateView, EditProductUpdateView


app_name = 'catalog'


urlpatterns = [
    path('', IndexListView.as_view(), name='homepage'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/create/', CreateProductCreateView.as_view(), name='create_product'),
    path('catalog/<slug:product_slug>/', ProductDetailView.as_view(), name='product_info'),
    path('catalog/edit/<slug:product_slug>/', EditProductUpdateView.as_view(), name='edit_product'),
]
