# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audit_name', models.CharField(max_length=100)),
                ('audit_description', models.CharField(max_length=250)),
            ],
        ),
    ]
