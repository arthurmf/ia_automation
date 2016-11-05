from django import forms
from django.forms import ModelForm, Textarea
from project.models import Activity_Client, Activity_EY
from documents.models import Cache
from .models import Template
from django.contrib.auth.admin import User

#class EmailForm(forms.Form):
#    email = forms.EmailField(max_length=70)

class EmailForm(ModelForm):
    class Meta:
        model = Cache
        fields = ('ey_employee',)

class NewDocumentForm(ModelForm):
    class Meta:
        model = Template
        fields = ('audit_type', 'template_name','template_description','template_version','is_template')
        widgets = {
            'template_description': Textarea(attrs={'cols': 80, 'rows': 20})
        }
