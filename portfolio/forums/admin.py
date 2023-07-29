from django.contrib import admin

# Register your models here.
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('postName', 'name', 'email', 'body', 'isPlainText', 'create', 'updated', 'active', 'mainFeatured', 'featured')
    list_filter = ('active', 'create', 'updated')
    search_fields = ('postName', 'name', 'email', 'body')