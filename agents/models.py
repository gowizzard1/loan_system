from django.db import models
import datetime
# Create your models here.
class Agents(models.Model):
    agent_name = models.CharField(max_length=100)
    status = models.IntegerField()
    date_created = models.DateField(("Date"), default=datetime.date.today)