from __future__ import unicode_literals

from django.db import models
from audit.models import Type
from register.models import Client, Ey_employee
from status.models import List

# Tables related to Services
class Service_style(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=250)

class Activity(models.Model):
    project_name = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    audit = models.ForeignKey(Type, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    status = models.ForeignKey(List, on_delete=models.PROTECT)
    ey_employee_master = models.ForeignKey(Ey_employee, on_delete=models.PROTECT)
    service_style = models.ForeignKey(Service_style, on_delete=models.PROTECT)
    activity_description = models.CharField(max_length=4000)

