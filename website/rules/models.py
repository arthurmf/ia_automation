from __future__ import unicode_literals

from django.db import models
from documents.models import Template

# Tables related to Operation Rules
class Operator(models.Model):
    operator_description = models.CharField(max_length=250)

    def __str__(self):
        return self.operator_description

class Definitions(models.Model):
    definition_name = models.CharField(max_length=250)
    definition_description = models.CharField(max_length=250)
    definition_column = models.CharField(max_length=100)
    definition_line = models.CharField(max_length=100)
    definition_rule = models.CharField(max_length=100)
    definition_operator = models.ForeignKey(Operator, on_delete=models.PROTECT)
    template = models.ForeignKey(Template, on_delete=models.PROTECT)
    definition_result = models.CharField(max_length=2000)

    def __str__(self):
        return self.definition_name