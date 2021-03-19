from django.forms import forms
from django.forms.fields import CharField, EmailField
from django.forms.widgets import PasswordInput


class users(forms.Form):
    username=EmailField()
    password=PasswordInput()