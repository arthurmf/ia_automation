# -*- coding: utf-8 -*- 
from django.forms import ModelForm
from project.models import Activity
from django import forms
from django.core.validators import MinLengthValidator

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('project_name','activity_description', 'start_date', 'end_date')


class Template_Upload(forms.Form):
    upload = forms.FileField(label='', required=False)
    
