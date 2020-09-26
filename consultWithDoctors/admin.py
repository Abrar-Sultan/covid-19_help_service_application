from django.contrib import admin
from .models import ConsultWithDoctor


class ConsultWithDoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'nid', 'blood_group')


admin.site.register(ConsultWithDoctor, ConsultWithDoctorAdmin)
