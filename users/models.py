from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]


class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    # gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True )
