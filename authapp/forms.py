from distutils.command.upload import upload
from pyexpat import model
from attr import fields
from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Info

class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username' ,'email',]
        labels = {'email':'Email'}
        labels = {'username':'Name'}



class SignupInfoForm(forms.ModelForm):
   class Meta:
     model=Info
     fields=['image']