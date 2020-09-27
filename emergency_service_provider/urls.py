from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.emergency_service_provider_home),
    path('available_ambulance', views.available_ambulance),
    path('reserved_ambulance', views.reserved_ambulance),
    path('confirm_reservation', views.confirm_reservation),
    path('search_ambulance', views.search_ambulance),
    path('delete_request_form', views.delete_request_form),
    path('delete_request', views.delete_request),
    path('available_oxygen_cylinder', views.available_oxygen_cylinder),
    path('reserved_oxygen_cylinder', views.reserved_oxygen_cylinder),
    path('confirm_oxygen_reservation', views.confirm_oxygen_reservation),
    path('search_oxygen_cylinder', views.search_oxygen_cylinder),
    path('delete_oxygen_request_form', views.delete_oxygen_request_form),
    path('delete_oxygen_request', views.delete_oxygen_request),

]
