# -*- coding: utf-8 -*- 
from django.forms import ModelForm
from project.models import Activity
from django import forms


class ActivityForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        initial = {
               'status': 1,
               'service_style': 1
              }
        if kwargs.has_key('initial'):
            kwargs['initial'].update(initial)
        else:
            kwargs['initial'] = initial
        # Initializing form only after you have set initial dict
        super(ActivityForm,self).__init__(*args, **kwargs)
        
        self.fields['status'].widget = forms.HiddenInput()
        self.fields['service_style'].widget = forms.HiddenInput()
        
    class Meta:
        model = Activity
        fields = ('project_name','activity_description', 'start_date', 'end_date', 'client', 'audit', 'ey_employee_master', 'status', 'service_style')
        
class Template_Upload(forms.Form):
    upload = forms.FileField(label='', required=False)


class Validation_Form(forms.Form):
    validate = forms.BooleanField(initial=True, widget=forms.HiddenInput())
    
    def __init__(self, *args, **kwargs):
        super(Validation_Form,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'id': 'validate_id'}) 