from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    address1 = forms.CharField()
    address2 = forms.CharField()
    city = forms.CharField()
    zip = forms.IntegerField()
