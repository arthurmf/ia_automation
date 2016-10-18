# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20161018_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Client_type'),
        ),
        migrations.AlterField(
            model_name='client_employee',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Client'),
        ),
        migrations.AlterField(
            model_name='client_employee',
            name='client_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Client_position'),
        ),
        migrations.AlterField(
            model_name='ey_employee',
            name='ey_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Ey_position'),
        ),
    ]
