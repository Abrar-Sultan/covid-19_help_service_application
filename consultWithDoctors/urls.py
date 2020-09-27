from django.urls import path
from . import views

"""
@route localhost:8000/consult
@desc home url of the consultWithDoctors Page
"""

urlpatterns = [
    path('', views.index)
]
