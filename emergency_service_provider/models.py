from django.db import models


class AvailableAmbulance(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    hospital_name = models.CharField(max_length=30)
    ambulance_type = models.CharField(max_length=20)
    ambulance_number = models.CharField(max_length=30)
    price = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=254)
    is_available = models.BooleanField()


class ReserveAmbulance(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    username = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=30)
    ambulance_type = models.CharField(max_length=20)
    ambulance_number = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    patient_name = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    nid = models.CharField(max_length=150)
    location = models.CharField(max_length=255)
    bkash_number = models.CharField(max_length=15)
    bkash_transaction_id = models.CharField(max_length=20)


class AvailableOxygenCylinder(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    company_name = models.CharField(max_length=30)
    cylinder_size = models.CharField(max_length=20)
    cylinder_number = models.CharField(max_length=30)
    price = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=254)
    is_available = models.BooleanField()


class ReserveOxygenCylinder(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    username = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    cylinder_size = models.CharField(max_length=20)
    cylinder_number = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    patient_name = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    nid = models.CharField(max_length=150)
    location = models.CharField(max_length=255)
    bkash_number = models.CharField(max_length=15)
    bkash_transaction_id = models.CharField(max_length=20)
