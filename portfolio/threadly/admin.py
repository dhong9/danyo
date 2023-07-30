from django.contrib import admin

# Register your models here.
from .models import Project, Comment, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'pageName', 'create', 'active', 'isPlainText')
    list_filter = ('active', 'create', 'updated')
    search_fields = ('name', 'email', 'body')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'query_txt', 'add_time')
    search_fields = ('full_name', 'email', 'query_txt', 'add_time')