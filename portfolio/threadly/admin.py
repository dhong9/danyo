from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'pageName', 'create', 'active', 'isPlainText')
    list_filter = ('active', 'create', 'updated')
    search_fields = ('name', 'email', 'body')