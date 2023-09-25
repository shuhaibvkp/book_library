from django import forms
from .models import *
from django.contrib.auth.models import User

class authregform(forms.ModelForm):
    class Meta:
        model= User
        fields= ['username','email','password']


class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    # re_password=forms.CharField(max_length=

class bookform(forms.ModelForm):
    class Meta:
        model = addbook
        fields = '__all__'
