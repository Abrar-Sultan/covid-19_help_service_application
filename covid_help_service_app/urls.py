"""covid_help_service_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('home.urls')),
                  path('admin/', admin.site.urls),
                  path('home/', include('home.urls')),
                  path('plasma_service/', include('plasma_service.urls')),
                  path('emergency_service_provider/', include('emergency_service_provider.urls')),
                  path('Test_Online/', include('covid_test.urls')),
                  path('find_medicine/', include('find_medicine.urls')),
                  path('Reserve_Page/', include('reserve_icu_and_hospital_bed.urls')),
                  path('blog/', include('Blog.urls')),
                  path('consult/', include('consultWithDoctors.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
