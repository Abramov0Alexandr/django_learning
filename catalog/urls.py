from django.urls import path
from catalog.views import IndexListView, ContactsView, ProductDetailView


app_name = 'catalog'


urlpatterns = [
    path('', IndexListView.as_view(), name='homepage'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/<slug:product_slug>/', ProductDetailView.as_view(), name='product_info'),
]
