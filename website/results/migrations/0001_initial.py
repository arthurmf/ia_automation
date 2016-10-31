# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_definition_name', models.CharField(max_length=100)),
                ('log_definition_description', models.CharField(max_length=250)),
                ('log_definition_column', models.CharField(max_length=10)),
                ('log_definition_line', models.CharField(max_length=10)),
                ('log_definition_rule', models.CharField(max_length=2000)),
                ('log_client_action', models.CharField(max_length=2000)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.Activity')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Client')),
            ],
        ),
    ]
