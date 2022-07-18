from django.db import models
from django.contrib.auth import get_user_model

PROPERTY_PURPOSE_SELECT = [
    ("rent", "Rent"),
    ("sale", "Sale"),
    ("shortlet", "Shortlet"),
    ("land", "Land"),
]
PROPERTY_TYPE_SELECT = [
    ("flat", "Flat"),
    ("land", "Land"),
    ("house", "House"),
    ("commercial", "Commercial"),
]

# Create your models here.
class Property(models.Model):
    first_title = models.CharField(max_length=250, blank=False, null=False)
    second_title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(
        blank=False, null=False, default="This is the description"
    )
    bedroom_count = models.IntegerField(default=1)
    bathroom_count = models.IntegerField(default=1)
    toilet_count = models.IntegerField(default=1)
    parking_space = models.IntegerField(default=1)
    seller = models.ForeignKey(
        get_user_model(), default=1, null=True, on_delete=models.SET_NULL
    )
    price = models.IntegerField(blank=False, null=False, default=100000000)
    location = models.CharField(
        max_length=250, blank=True, null=False, default="Sangotedo, Lagos"
    )
    purpose = models.CharField(
        choices=PROPERTY_PURPOSE_SELECT, max_length=20, default="forSale"
    )
    type = models.CharField(choices=PROPERTY_TYPE_SELECT, max_length=20, default="flat")
    address = models.CharField(
        max_length=250, default="No 23, Alagbado, Lagos", blank=False, null=False
    )
    added = models.DateTimeField(auto_now=True)

    cover_photo = models.ImageField(default="/download.jpg")

    def __str__(self):
        return self.first_title


# class PhotoBook(models.Model):
#     book = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="photos")
#     image = models.ImageField(blank=True, null=True)

#     def __str__(self):
#         return self.image
