from django.urls import path
from . import views

"""
@route localhost:8000/blog
@desc home url of the Blog Page
"""

urlpatterns = [
    path('', views.blog)
]
