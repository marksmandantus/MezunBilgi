from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Person

from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Person
        fields = ('email', 'tc_kimlik_no', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = Person.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} already in use.')
    
    def clean_tc_kimlik_no(self):
        tc_kimlik_no = self.cleaned_data['tc_kimlik_no']
        try:
            user = Person.objects.get(tc_kimlik_no=tc_kimlik_no)
        except Exception as e:
            return tc_kimlik_no
        raise forms.ValidationError(f'TC kimlik numarası {tc_kimlik_no} already in use.')


class kaydet(forms.Form):
    email = forms.CharField(max_length=40)
    telefon = forms.CharField(max_length=11)
    adres = forms.CharField(max_length=70)

    # Diğer alanlar



