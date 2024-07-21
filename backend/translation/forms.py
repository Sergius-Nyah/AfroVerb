from django import forms
from django.core import validators

class UserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not email:
            raise forms.ValidationError('Email is required.')
        if not password:
            raise forms.ValidationError('Password is required.')
