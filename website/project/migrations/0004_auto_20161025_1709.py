# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20161018_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clientes_projeto', to='register.Client'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='ey_employee_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Ey_employee'),
        ),
    ]
