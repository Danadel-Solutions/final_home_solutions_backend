from django.db import models
from django.contrib.auth import get_user_model

PROPERTY_TYPE_SELECT = [
    ('Rent', 'rent'),
    ('For Sale', 'forSale'),
    ('Shortlet', 'Shortlet'),
    ('Land', 'land'),
]

# Create your models here.
class Property(models.Model):
    first_title = models.CharField(max_length=250, blank = False, null = False)
    second_title = models.CharField(max_length=250, blank = False, null = False)
    description = models.TextField (blank= False, null = False, default='This is the description')
    bedroom_count = models.IntegerField(default = 1)
    bathroom_count = models.IntegerField(default = 1)
    toilet_count = models.IntegerField(default = 1)
    parking_space = models.IntegerField(default = 1)
    seller = models.ForeignKey(get_user_model(), default=1, null = True, on_delete=models.SET_NULL)
    price = models.IntegerField(blank = False, null = False, default = 100000000)
    location = models.CharField(max_length=250, blank = True, null = False, default = 'Sangotedo, Lagos')
    type = models.CharField(choices=PROPERTY_TYPE_SELECT, max_length = 20, default='forSale')
    added = models.DateTimeField(auto_now=True)

    cover_photo = models.ImageField()
    def __str__(self):
        return self.first_title

class PhotoBook(models.Model):
    book = models.ForeignKey(Property, on_delete= models.CASCADE, related_name="photos")
    image = models.ImageField(blank = True, null = True)