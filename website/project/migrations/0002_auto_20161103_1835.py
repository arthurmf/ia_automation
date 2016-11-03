# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20161031_1027'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Activity_EY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_code',
            field=models.CharField(default='XXXXXXX', max_length=250),
        ),
        migrations.AddField(
            model_name='activity_ey',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Activity'),
        ),
        migrations.AddField(
            model_name='activity_ey',
            name='ey_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Ey_employee'),
        ),
        migrations.AddField(
            model_name='activity_client',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Activity'),
        ),
        migrations.AddField(
            model_name='activity_client',
            name='client_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Client_employee'),
        ),
    ]
