from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30)
    availability = models.BooleanField(default=True)
    needing_repair = models.BooleanField(default=True)
    durability = models.IntegerField()
    max_durability = models.IntegerField()
    mileage = models.IntegerField(null=True)
    price = models.IntegerField()
    minimum_rent_period = models.IntegerField()