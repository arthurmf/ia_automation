from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Type(models.Model):
    audit_name = models.CharField(max_length=100)
    audit_description = models.CharField(max_length=250)

    def __str__(self):
        return self.audit_name
