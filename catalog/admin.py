from django.contrib import admin
from catalog.models import Product, Category


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
