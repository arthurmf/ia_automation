# -*- coding: utf-8 -*- 
from django.forms import ModelForm
from project.models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude = ('nada',)