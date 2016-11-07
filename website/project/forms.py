# -*- coding: utf-8 -*- 
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from project.models import Activity
from register.models import Ey_employee
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
        #self.fields['ey_employee_master'] = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=1))

    #def return_full_name(queryset):
    #    full_name_list = []
    #    for query in queryset:
    #        full_name_list.append(query.first_name + " " + query.last_name)
    #    return full_name_list


    class Meta:
        model = Activity
        fields = (
        'project_name', 'activity_description', 'start_date', 'end_date', 'client', 'audit', 'ey_employee_master',
        'status', 'service_style')
        widgets = {
            'activity_description': Textarea(attrs={'cols': 80, 'rows': 20}),
            'start_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class Template_Upload(forms.Form):
    upload = forms.FileField(label='', required=False)


class Validation_Form(forms.Form):
    validate = forms.BooleanField(initial=True, widget=forms.HiddenInput())
    
    def __init__(self, *args, **kwargs):
        super(Validation_Form,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'id': 'validate_id'}) 