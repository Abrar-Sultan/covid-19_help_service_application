from django.db import models


class PlasmaRequest(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects
    """
    username = models.CharField(max_length=254)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    nid = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=128)
    location = models.CharField(max_length=2083)
    image = models.ImageField(upload_to='covid_pos_report')


class PlasmaDonate(models.Model):
    """
     This class is extended from the Model class so it has all the functionality
     of the model class.


     this class used to create objects
     """
    username = models.CharField(max_length=254)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    nid = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=128)
    location = models.CharField(max_length=2083)
    image = models.ImageField(upload_to='covid_neg_report')
