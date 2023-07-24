from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Person, Graduate



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    ad = forms.CharField(max_length=60, help_text='Required. Add a valid first name')
    soyad = forms.CharField(max_length=60, help_text='Required. Add a valid last name')
    telefon = forms.CharField(max_length=11, help_text='Required. Add a valid phone number')
    username = forms.CharField(max_length=60, help_text='Required. Add a valid username')

    class Meta:
        model = Person
        fields = ('email', 'ad', 'soyad', 'telefon', 'password1', 'password2', 'tc_kimlik_no', 'universite')

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
    
    def clean_telefon(self):
        telefon = self.cleaned_data['telefon']
        # ÖZEL DOĞRULAMALAR BURAYA
        return telefon

    def clean_ad(self):
        ad = self.cleaned_data['ad']
        return ad

    def clean_soyad(self):
        soyad = self.cleaned_data['soyad']
        return soyad
    
    def clean_tc_kimlik_no(self):
        tc_kimlik_no = self.cleaned_data['tc_kimlik_no']
        return tc_kimlik_no
    
    def clean_username(self):
        username = self.cleaned_data['username']
        return username
    
    def clean_universite(self):
        universite = self.cleaned_data['universite']
        return universite
    

    

class GraduateForm(forms.ModelForm):
    class Meta:
        model = Graduate
        fields = ('mezun_yili', 'mezun_bolum', 'mezun_derece', )

    def clean_mezun_yili(self):
        mezun_yili = self.cleaned_data['mezun_yili']
        return mezun_yili
    
    def clean_mezun_bolum(self):
        mezun_bolum = self.cleaned_data['mezun_bolum']
        return mezun_bolum
    
    def clean_mezun_derece(self):
        mezun_derece = self.cleaned_data['mezun_derece']
        return mezun_derece


class kaydet(forms.Form):
    email = forms.CharField(max_length=40)
    telefon = forms.CharField(max_length=11)
    adres = forms.CharField(max_length=70)

    # Diğer alanlar



