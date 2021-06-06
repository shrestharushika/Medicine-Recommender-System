from django import forms
from RS.models import Doctor
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.db import models


class UserForm(UserCreationForm):
   
    class Meta:
        model=User
        fields=('username','email','password1','password2',)

class queryForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=('query',)        
