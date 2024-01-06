from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from .models import User
from .models import Diseases


class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control'}),
                   'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
                   }

    def clean(self):
        cleaned_data = super(signupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )