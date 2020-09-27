from django.contrib import admin
from .models import Blog


"""
admin display keys for the Blog model
"""


class BlogAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'age', 'story')


admin.site.register(Blog, BlogAdmin)
