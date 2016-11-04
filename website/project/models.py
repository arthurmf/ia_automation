# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.db import models
from audit.models import Type
from register.models import Client, Ey_employee, Client_employee
from status.models import List

# Tables related to Services
class Service_style(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=250)

    def __str__(self):
        return self.service_name

class Activity(models.Model):
    project_name = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    audit = models.ForeignKey(Type, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='clientes_projeto')
    status = models.ForeignKey(List, on_delete=models.PROTECT)
    ey_employee_master = models.ForeignKey(Ey_employee, on_delete=models.PROTECT)
    service_style = models.ForeignKey(Service_style, on_delete=models.PROTECT)
    activity_description = models.CharField(max_length=4000)
    activity_code = models.CharField(max_length=250, default="XXXXXXX")

    def __str__(self):
        return self.project_name
        
    def return_list(self):
        return [self.project_name,
                self.activity_description,
                self.client,
                self.ey_employee_master,
                self.start_date,
                self.end_date,
                self.audit,
                self.status]
    
    #def nome_cliente(self, cliente_projeto):
       # return Activity(project_name=self, client=cliente_projeto).get

class Activity_EY(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    ey_employee = models.ForeignKey(Ey_employee, on_delete=models.PROTECT)

class Activity_Client(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    client_employee = models.ForeignKey(Client_employee, on_delete=models.PROTECT)
