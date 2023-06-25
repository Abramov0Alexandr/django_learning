from django.contrib import admin
from blog.models import FashionBlog


@admin.register(FashionBlog)
class FashionBlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_published', 'view_count')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}
