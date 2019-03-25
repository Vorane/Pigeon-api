from django.db import models
from authentication.models import User
from store_listing.models import Outlet, Store

# Create your models here.
class Attendant(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),    
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    outlet = models.ForeignKey(Outlet, on_delete=models.DO_NOTHING)

    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    other_names = models.CharField(max_length=255,blank=True)
    national_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50,blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,blank=True, max_length=30)

    def __str__(self):
        return str( self.first_name + " " + self.last_name + " - " + self.outlet.display_name)

class Manager(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),    
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)

    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    other_names = models.CharField(max_length=255,blank=True)
    national_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50,blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,blank=True, max_length=30)
