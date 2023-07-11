from django.urls import path
from catalog import views

app_name = 'catalog'


urlpatterns = [
    path('', views.IndexListView.as_view(), name='homepage'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('catalog/create/', views.ProductCreateView.as_view(), name='create_product'),
    path('catalog/<slug:product_slug>/', views.ToggleSalesStatusView.as_view(), name='toggle_status'),
    path('catalog/view/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_info'),
    path('catalog/delete/<slug:product_slug>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('catalog/edit/<slug:product_slug>/', views.ProductUpdateView.as_view(), name='edit_product'),
]
