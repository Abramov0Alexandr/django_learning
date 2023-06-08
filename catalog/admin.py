from django.contrib import admin
from catalog.models import Product, Category, FashionBlog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'category')
    list_display_links = ('title',)
    list_editable = ('price',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(FashionBlog)
class FashionBlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_published', 'view_count')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}
