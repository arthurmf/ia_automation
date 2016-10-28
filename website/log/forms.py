from django.contrib.auth.forms import AuthenticationForm 
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'password'}))
