from django import forms
from basic_app.models import *
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class formname(forms.Form):
    name=forms.CharField()
    technology=forms.CharField()
    email=forms.EmailField()

class modelname(forms.ModelForm):
    class Meta():
        model=modelpage
        fields='__all__'

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')

