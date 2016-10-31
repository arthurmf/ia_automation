from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Client_employee, Ey_employee
from django import forms

class ClientEmployeeUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientEmployeeUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined')
        #exclude = ('last_name',)
        
class ClientEmployeeForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        initial = {
               'client_user': 1,
              }
        if kwargs.has_key('initial'):
            kwargs['initial'].update(initial)
        else:
            kwargs['initial'] = initial
        # Initializing form only after you have set initial dict
        super(ClientEmployeeForm,self).__init__(*args, **kwargs)
        
        self.fields['client_user'].widget = forms.HiddenInput()
        
    class Meta:
        model = Client_employee
        fields = ('client_position', 'client_employee_telephone', 'client', 'client_user')

class EyEmployeeUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EyEmployeeUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined')
        #exclude = ('last_name',)
        
class EyEmployeeForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        initial = {
               'ey_employee_user': 1,
              }
        if kwargs.has_key('initial'):
            kwargs['initial'].update(initial)
        else:
            kwargs['initial'] = initial
        # Initializing form only after you have set initial dict
        super(EyEmployeeForm,self).__init__(*args, **kwargs)
        
        self.fields['ey_employee_user'].widget = forms.HiddenInput()
        
    class Meta:
        model = Ey_employee
        fields = ('ey_position', 'ey_employee_telephone', 'ey_employee_user')

