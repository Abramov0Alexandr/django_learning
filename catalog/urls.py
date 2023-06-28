from django.urls import path
from catalog.views import IndexListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'catalog'


urlpatterns = [
    path('', IndexListView.as_view(), name='homepage'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/create/', ProductCreateView.as_view(), name='create_product'),
    path('catalog/<slug:product_slug>/', ProductDetailView.as_view(), name='product_info'),
    path('catalog/delete/<slug:product_slug>', ProductDeleteView.as_view(), name='delete_product'),
    path('catalog/edit/<slug:product_slug>/', ProductUpdateView.as_view(), name='edit_product'),
]
