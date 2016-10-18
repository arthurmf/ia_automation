from __future__ import unicode_literals

from django.db import models
from project.models import Activity
from register.models import Client, Ey_employee
from documents.models import Template, Received
from rules.models import Operator

# Create your models here.
class Log(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    ey_employee = models.ForeignKey(Ey_employee, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    log_result = models.BooleanField
    log_definition_name = models.CharField(max_length=100)
    log_definition_description = models.CharField(max_length=250)
    log_definition_column = models.CharField(max_length=10)
    log_definition_line = models.CharField(max_length=10)
    log_definition_rule = models.CharField(max_length=2000)
    definition_operator = models.ForeignKey(Operator, on_delete=models.PROTECT)
    log_client_action = models.CharField(max_length=2000)
    log_client_action_date = models.DateField
    received = models.ForeignKey(Received, on_delete=models.PROTECT)
    template = models.ForeignKey(Template, on_delete=models.PROTECT)
    last_modified = models.DateTimeField(auto_now=True)
