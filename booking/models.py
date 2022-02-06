from django.db import models
from products.models import Product

# Create your models here.
class Booking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)