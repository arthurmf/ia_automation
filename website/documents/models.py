from __future__ import unicode_literals

from django.db import models
from audit.models import Type
from register.models import Ey_employee, Client_employee
from project.models import Activity

# Tables related to documents
class Template(models.Model):
    audit_type = models.ForeignKey(Type, on_delete=models.PROTECT)
    template_name = models.CharField(max_length=250)
    template_description = models.CharField(max_length=250)
    template_format = models.CharField(max_length=25)
    template_version = models.CharField(max_length=10)
    template_author = models.ForeignKey(Ey_employee, on_delete=models.PROTECT)
    template_path = models.CharField(max_length=500)
    
    def __str__(self):
        return self.template_name

class Request(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    client_employee = models.ForeignKey(Client_employee, on_delete=models.PROTECT)
    template = models.ForeignKey(Template, on_delete=models.PROTECT)
    ey_employee = models.ForeignKey(Ey_employee, on_delete=models.PROTECT)

class Received(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    client_employee = models.ForeignKey(Client_employee, on_delete=models.PROTECT)
    ey_employee = models.ForeignKey(Ey_employee, on_delete=models.PROTECT)
    received_name = models.CharField(max_length=100)
    received_description = models.CharField(max_length=250)
    received_format = models.CharField(max_length=25)
    received_version = models.CharField(max_length=10)
    received_path = models.CharField(max_length=500)
    received_answer = models.BooleanField
    template = models.ForeignKey(Template, on_delete=models.PROTECT)
