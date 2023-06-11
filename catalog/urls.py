from django.urls import path
from catalog.views import IndexListView, contacts, \
    ProductDetailView, FashionBlogView, BlogDetailView, \
    AddPostCreateView, DevelopingPostsView

# BlogCreateView add_post BlogCreateView.as_view()

urlpatterns = [
    path('', IndexListView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<slug:product_slug>/', ProductDetailView.as_view(), name='product_info'),
    path('blog/', FashionBlogView.as_view(), name='blog'),
    path('blog/<slug:blog_slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', AddPostCreateView.as_view(),  name='blog_create'),
    path('edit/', DevelopingPostsView.as_view(), name='developing_posts'),

]
