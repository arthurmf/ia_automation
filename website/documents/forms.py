from django import forms
from django.forms import ModelForm, models
from project.models import Activity_Client, Activity_EY
from documents.models import Cache
from django.contrib.auth.admin import User

#class EmailForm(forms.Form):
#    email = forms.EmailField(max_length=70)

class EmailForm(ModelForm):
    class Meta:
        model = Cache
        fields = ('ey_employee',)