# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20161018_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Received',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_name', models.CharField(max_length=100)),
                ('received_description', models.CharField(max_length=250)),
                ('received_format', models.CharField(max_length=25)),
                ('received_version', models.CharField(max_length=10)),
                ('received_path', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='template',
            name='template_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Ey_employee'),
        ),
    ]
