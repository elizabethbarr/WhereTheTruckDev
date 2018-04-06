from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class VendorListing(models.Model):
    vendor_name = models.CharField(max_length=50)
    vendor_image = models.ImageField(upload_to='uploads', blank=True, null=True)
    vendor_email = models.EmailField(max_length=30)
    vendor_phone = models.IntegerField()
    vendor_bio = models.CharField(max_length=110)
    date_updated = models.DateTimeField(auto_now_add=True)
    todays_location = models.CharField(max_length=60)
    todays_hours = models.CharField(max_length=60)
    serving_today = models.TextField(max_length=None)
    truck_service = models.BooleanField(default=True)
    cart_service = models.BooleanField(default=False)
    popup_service = models.BooleanField(default=False)
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/uploads/default.png"

    def __str__(self):
        return self.vendor_name
