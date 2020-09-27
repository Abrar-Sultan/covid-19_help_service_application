from django.db import models

class OnlineTest(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nid_or_birth_certificate = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)


