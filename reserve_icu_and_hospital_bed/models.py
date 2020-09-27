from django.db import models

# Create your models here.



class AvailableICU(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    hospital_name = models.CharField(max_length=30)
    icu_type = models.CharField(max_length=20)
    price = models.CharField(max_length=5)
    address = models.CharField(max_length=30)
    is_available = models.CharField(max_length=5)

class BookingICU(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=30)
    icu_type = models.CharField(max_length=20)
    price = models.CharField(max_length=5)
    patient_name = models.CharField(max_length=30)
    patient_blood_group = models.CharField(max_length=5)
    patient_age = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=15)
    bkash_number = models.CharField(max_length=15)
    bkash_transaction_id = models.CharField(max_length=20)
    is_available = models.CharField(max_length=5)
    previous_id = models.CharField(max_length=5)

class AvailableHospitalBed(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    hospital_name = models.CharField(max_length=30)
    bed_number = models.CharField(max_length=30)
    price_per_day = models.CharField(max_length=5)
    available_ac = models.CharField(max_length=5)
    address = models.CharField(max_length=30)
    is_available = models.CharField(max_length=5)

class BookingHospitalBed(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=30)
    price_per_day = models.CharField(max_length=5)
    bed_number = models.CharField(max_length=30)
    available_ac = models.CharField(max_length=5)
    patient_name = models.CharField(max_length=30)
    patient_blood_group = models.CharField(max_length=5)
    patient_age = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=15)
    bkash_number = models.CharField(max_length=15)
    bkash_transaction_id = models.CharField(max_length=20)
    is_available = models.CharField(max_length=5)
    previous_id = models.CharField(max_length=5)