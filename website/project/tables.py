# -*- coding: utf-8 -*-

import django_tables2 as tables
from project.models import Activity


class SimpleTable(tables.Table):
    #teste = tables.Column()
    #teste2 = tables.CheckBoxColumn(attrs={'name':'my_checkbox'})
    
    
    #class Meta:
        #model = Activity
        #exclude = ['id','service_style']
        #sequence = ['project_name','activity_description', 'client', 'ey_employee_master']

    a = tables.Column()
    b = tables.CheckBoxColumn(attrs={'name': 'my_chkbox'})