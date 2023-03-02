from django.core import validators
from django import forms
from .models import Client


class ClientRegistration(forms.ModelForm):
    class Meta:
        model=Client
        fields = ['Name','Email','Location']
        widgets={
        'Name': forms.TextInput(attrs={'class':'form-control'}),
        'Email': forms.EmailInput(attrs={'class':'form-control'}),
        'Location': forms.TextInput(attrs={'class':'form-control'}),
        }
