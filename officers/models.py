from django.db import models

import datetime
# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    nationa_id = models.CharField(max_length=20)
    status = models.SmallIntegerField()

    class Meta:
        db_table = "customers"

class Agent(models.Model):
    agent_name = models.CharField(max_length=100)
    nationa_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    status = models.IntegerField()
    date_created = models.DateField(("Date"), default=datetime.date.today) 

    class Meta:
        db_table = "agents"



class Officer(models.Model):
    officer_name = models.CharField(max_length=100)
    nationa_id = models.CharField(max_length=20)
    status = models.IntegerField()
    date_created = models.DateField(("Date"), default=datetime.date.today)

    class Meta:
        db_table = "officers"

class Loan(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer,default=0,on_delete=models.SET_DEFAULT)
    agent_id =models.ForeignKey(Agent,default=0,on_delete=models.SET_DEFAULT)
    office_id = models.ForeignKey(Officer,default=0,on_delete=models.SET_DEFAULT)
    amount = models.IntegerField()
    date_issued = models.DateField(("Date"), default=datetime.date.today)
    date_due = models.DateField(("Date"), default=datetime.date.today)
    interest = models.IntegerField()

    class Meta:
        db_table = "loans"



