from django.db import models
import datetime
# Create your models here.

class Customers(models.Model):
    customer_name = models.CharField(max_length=100)
    status = models.SmallIntegerField()

class Agents(models.Model):
    agent_name = models.CharField(max_length=100)
    status = models.IntegerField()
    date_created = models.DateField(("Date"), default=datetime.date.today)  


class Officers(models.Model):
    officer_name = models.CharField(max_length=100)
    status = models.IntegerField()
    date_created = models.DateField(("Date"), default=datetime.date.today)

class Loans(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customers,default=0,on_delete=models.SET_DEFAULT)
    agent_id =models.ForeignKey(Agents,default=0,on_delete=models.SET_DEFAULT)
    office_id = models.ForeignKey(Officers,default=0,on_delete=models.SET_DEFAULT)
    amount = models.IntegerField()
    date_issued = models.DateField(("Date"), default=datetime.date.today)
    date_due = models.DateField(("Date"), default=datetime.date.today)
    interest = models.IntegerField()

    def __str__(self):
        return self.customer_name


