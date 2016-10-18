from __future__ import unicode_literals

from django.db import models

# Tables related to Client employee
class Client_type(models.Model):
    client_type_description = models.CharField(max_length=250)

class Client_position(models.Model):
    client_position_description = models.CharField(max_length=250)

class Client(models.Model):
    client_name = models.CharField(max_length=250)
    client_type = models.ForeignKey(Client_type, on_delete=models.PROTECT)

class Client_employee(models.Model):
    client_employee_name = models.CharField(max_length=250)
    client_position = models.ForeignKey(Client_position, on_delete=models.PROTECT)
    client_employee_email = models.CharField(max_length=100)
    client_employee_telephone = models.CharField(max_length=25)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

# Tables related to EY employee
class Ey_position(models.Model):
    ey_position_description = models.CharField(max_length=250)

class Ey_employee(models.Model):
    ey_employee_name = models.CharField(max_length=250)
    ey_position = models.ForeignKey(Ey_position, on_delete=models.PROTECT)
    ey_employee_email = models.CharField(max_length=100)
    ey_employee_telephone = models.CharField(max_length=25)

