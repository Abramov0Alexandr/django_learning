from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views

app_name = 'catalog'


urlpatterns = [
    path('', views.IndexListView.as_view(), name='homepage'),
    path('contacts/', cache_page(60)(views.ContactsView.as_view()), name='contacts'),
    path('catalog/create/', views.ProductCreateView.as_view(), name='create_product'),
    path('catalog/category/<int:cat_id>', views.show_category, name='show_category'),
    path('catalog/<slug:product_slug>/', views.ToggleSalesStatusView.as_view(), name='toggle_status'),
    path('catalog/view/<slug:product_slug>/', cache_page(60)(views.ProductDetailView.as_view()), name='product_info'),
    path('catalog/delete/<slug:product_slug>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('catalog/edit/<slug:product_slug>/', views.ProductUpdateView.as_view(), name='edit_product'),
]
