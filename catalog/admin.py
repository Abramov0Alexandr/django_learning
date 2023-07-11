from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'category', 'in_stock')
    list_display_links = ('title',)
    list_editable = ('price', 'in_stock')
    list_filter = ('category',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Version)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'version_number', 'version_title', 'is_active', )
    list_display_links = ('version_title',)
    list_editable = ('is_active', )
