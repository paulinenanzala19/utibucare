from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from.models import *

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
