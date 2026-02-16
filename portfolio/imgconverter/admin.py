from django.contrib import admin

# Register your models here.
from .models import ImgConverter

@admin.register
class ImgConverterAdmin(admin.ModelAdmin):
    list_display = ('date', 'image')
    search_fields = ('date', 'image')