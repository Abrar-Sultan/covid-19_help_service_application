from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_medicine_form),
    path('search_medicine', views.search_medicine),

]
