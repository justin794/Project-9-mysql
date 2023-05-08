from django.db import models

# Create your models here.

class Product(models.Model):
    pid = models.CharField(max_length=10)
    pname = models.CharField(max_length=20)
    product_quantity = models.PositiveBigIntegerField()
    manufacturer = models.CharField(max_length=20)
    mfd = models.DateField()
    