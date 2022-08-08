from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app import models
#User,UserProfileInfo
class FormName(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = models.UserProfileInfo
        fields = ('portfolio_site','profile_pic')
