from django.db import models


class ConsultWithDoctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    nid = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
