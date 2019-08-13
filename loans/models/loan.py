from django.db import models
import datetime
# Create your models here.
class Loan(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_id = models.ForeignKey(customer,on_delete=CASCADE)
    agent_id =models.ForeignKey(agent,on_delete=CASCADE)
    office_id = models.ForeignKey(officer,on_delete=CASCADE)
    amount = models.IntegerField()
    date_issued = models.DateField(("Date"), default=datetime.date.today)
    date_due = models.DateField(("Date"), default=datetime.date.today)
    interest = models.IntegerField())

    def __str__(self):
        retun self.name