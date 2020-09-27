from django.db import models


class FindMedicine(models.Model):
    """
        This class is extended from the Model class so it has all the functionality
        of the model class.


        this class used to create objects
        """
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    generic = models.CharField(max_length=50)
    indication = models.CharField(max_length=2083)
