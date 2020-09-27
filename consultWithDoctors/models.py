from django.db import models

"""
consultWithDoctor model with the field: name, age, nid, blood_group
"""


class ConsultWithDoctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    nid = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
