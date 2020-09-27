from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.plasma_home),
    path('request_plasma_form', views.request_plasma_form),
    path('request_plasma', views.request_plasma),
    path('show_plasma_request', views.show_plasma_request),
    path('search_request', views.search_request),
    path('delete_request_form', views.delete_request_form),
    path('delete_request', views.delete_request),
    path('donate_plasma_form', views.donate_plasma_form),
    path('donate_plasma', views.donate_plasma),
    path('show_plasma_donate_request', views.show_plasma_donate_request),
    path('search_donate_request', views.search_donate_request),
    path('delete_donate_request_form', views.delete_donate_request_form),
    path('delete_donate_request', views.delete_donate_request),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
