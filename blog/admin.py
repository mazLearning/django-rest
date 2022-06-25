from django.contrib import admin
from .models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['publish', 'status']
    search_fields = ['title', 'slug', 'description']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
