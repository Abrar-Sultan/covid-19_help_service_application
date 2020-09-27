from django.db import models


class AvailableAmbulance(models.Model):
    hospital_name = models.CharField(max_length=30)
    ambulance_type = models.CharField(max_length=20)
    ambulance_number = models.CharField(max_length=30)
    price = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=254)
    is_available = models.BooleanField()


class ReserveAmbulance(models.Model):
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
    company_name = models.CharField(max_length=30)
    cylinder_size = models.CharField(max_length=20)
    cylinder_number = models.CharField(max_length=30)
    price = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=254)
    is_available = models.BooleanField()


class ReserveOxygenCylinder(models.Model):
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
