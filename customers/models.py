from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_name = models.CharField(max_length=100)
    status= models.IntegerField()