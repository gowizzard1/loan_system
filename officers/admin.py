from django.contrib import admin
from officers.models import Customer
from officers.models import Agent
from officers.models import Loan
from officers.models import Officer

# Register your models here.

admin.site.register(Customer)
admin.site.register(Agent)
admin.site.register(Officer)
admin.site.register(Loan)