from django.contrib import admin
from .models import ConsultWithDoctor

"""
admin display keys for the consultWithDoctors model
"""


class ConsultWithDoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'nid', 'blood_group')


admin.site.register(ConsultWithDoctor, ConsultWithDoctorAdmin)
