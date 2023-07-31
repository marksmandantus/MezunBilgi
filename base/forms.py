from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Graduate



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    tc_kimlik_no = forms.CharField(max_length=11, help_text='Required. Add a valid tc_kimlik_no')
    
    class Meta:
        model = Person
        fields = ('email', 'password1', 'password2', 'tc_kimlik_no')

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
    email = forms.EmailField(required=False)
    ad = forms.CharField(required=False)
    soyad = forms.CharField(required=False)
    telefon = forms.CharField(required=False)
    username = forms.CharField(required=False)
    adres = forms.CharField(required=False)

    class Meta:
        model = Person
        fields = ('email', 'ad', 'soyad', 'telefon','username', 'adres')


class GraduateUpdateForm(forms.ModelForm):
    mezun_yili = forms.IntegerField(required=False)
    mezun_bolum = forms.CharField(required=False)
    mezun_derece = forms.IntegerField(required=False)
    class Meta:
        model = Graduate
        fields = ('mezun_yili', 'mezun_bolum', 'mezun_derece',)



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('profil',)

    






