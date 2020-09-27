from django.db import models

"""
Blog model with the field: name, age, nid, blood_group
"""


class Blog(models.Model):
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    story = models.CharField(max_length=1000)

