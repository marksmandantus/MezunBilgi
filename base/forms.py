from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Graduate



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    ad = forms.CharField(max_length=60, help_text='Required. Add a valid first name')
    soyad = forms.CharField(max_length=60, help_text='Required. Add a valid last name')
    telefon = forms.CharField(max_length=11, help_text='Required. Add a valid phone number')
    username = forms.CharField(max_length=60, help_text='Required. Add a valid username')

    class Meta:
        model = Person
        fields = ('email', 'ad', 'soyad', 'telefon', 'password1', 'password2', 'tc_kimlik_no','username')

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
        # Gerekirse telefon numarası için özel doğrulama kurallarını buraya ekleyin
        # ÖZEL DOĞRULAMALAR BURAYA
        return telefon

    def clean_ad(self):
        ad = self.cleaned_data['ad']
        # Gerekirse ad için özel doğrulama kurallarını buraya ekleyin
        return ad

    def clean_soyad(self):
        soyad = self.cleaned_data['soyad']
        # Gerekirse soyad için özel doğrulama kurallarını buraya ekleyin
        return soyad

    def clean_tc_kimlik_no(self):
        tc_kimlik_no = self.cleaned_data['tc_kimlik_no']
        # Gerekirse tc_kimlik_no için özel doğrulama kurallarını buraya ekleyin
        return tc_kimlik_no

    def clean_username(self):
        username = self.cleaned_data['username']
        # Gerekirse username için özel doğrulama kurallarını buraya ekleyin
        return username

      

class GraduateForm(forms.ModelForm):
    class Meta:
        model = Graduate
        fields = ('mezun_yili', 'mezun_bolum', 'mezun_derece', )

    def clean_mezun_yili(self):
        mezun_yili = self.cleaned_data['mezun_yili']
        # Gerekirse mezun_yili için özel doğrulama kurallarını buraya ekleyin
        return mezun_yili

    def clean_mezun_bolum(self):
        mezun_bolum = self.cleaned_data['mezun_bolum']
        # Gerekirse mezun_bolum için özel doğrulama kurallarını buraya ekleyin
        return mezun_bolum

    def clean_mezun_derece(self):
        mezun_derece = self.cleaned_data['mezun_derece']
        # Gerekirse mezun_derece için özel doğrulama kurallarını buraya ekleyin
        return mezun_derece
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    ad = forms.CharField()
    soyad = forms.CharField()
    telefon = forms.CharField()
    username = forms.CharField()
    adres = forms.CharField()
    website = forms.CharField()
    facebook = forms.CharField()
    instagram = forms.CharField()
    linkedin = forms.CharField()
    github = forms.CharField()

    class Meta:
        model = Person
        fields = ('email', 'ad', 'soyad', 'telefon','username', 'adres', 'website', 'facebook', 'instagram', 'linkedin', 'github')


class GraduateUpdateForm(forms.ModelForm):
    class Meta:
        model = Graduate
        fields = ('mezun_yili', 'mezun_bolum', 'mezun_derece',)



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('profil',)

    






