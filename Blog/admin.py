from django.contrib import admin
from .models import BlogItem


class BlogItemAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'age', 'story')


admin.site.register(BlogItem, BlogItemAdmin)
