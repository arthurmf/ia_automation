from __future__ import unicode_literals

from django.db import models

# Create your models here.
class List(models.Model):
    list_reference = models.CharField(max_length=10)
    list_description = models.CharField(max_length=250)

class Workflow(models.Model):
    workflow_current_status = models.CharField(max_length=10)
    workflow_next_status = models.CharField(max_length=10)

