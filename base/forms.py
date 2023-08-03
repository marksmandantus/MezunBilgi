from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Graduate, Location
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.core.exceptions import ValidationError

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'data-callback': 'onCaptchaSuccess'}))

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
        raise forms.ValidationError('Bu email ile önceden kayıt yapılmıştır.')
    
    def clean_tc_kimlik_no(self):
        tc_kimlik_no = self.cleaned_data['tc_kimlik_no'] 
        
        if len(tc_kimlik_no) != 11:
            raise forms.ValidationError('TC kimlik numarası 11 karakterden oluşmalıdır.')
        
        # Check if TC kimlik numarası contains only digits
        if not tc_kimlik_no.isdigit():
            raise forms.ValidationError('TC kimlik numarası yalnızca rakamlardan oluşmalıdır.')
        
         # Check if TC kimlik numarası is not negative
        if int(tc_kimlik_no) < 0:
            raise forms.ValidationError('TC kimlik numarası negatif bir sayı olamaz.')
        
        return tc_kimlik_no
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor. Lütfen aynı şifreyi girin.")
        return password2

      

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
    adres = forms.ModelChoiceField(queryset=Location.objects.all(), required=False)

    class Meta:
        model = Person
        fields = ('email', 'ad', 'soyad', 'telefon','username', 'adres')

    def clean_telefon(self):
        telefon = self.cleaned_data.get('telefon')
        if telefon and len(telefon) != 10:
            raise ValidationError("Telefon numarası 10 haneli olmalıdır.")
        return telefon

class ProfileUpdateForm(forms.ModelForm):

    profil = forms.ImageField(required=False)

    class Meta:
        model = Person
        fields = ('profil',)



class GraduateUpdateForm(forms.ModelForm):
    mezun_yili = forms.IntegerField(required=False)
    mezun_bolum = forms.CharField(required=False)
    mezun_derece = forms.IntegerField(required=False)
    class Meta:
        model = Graduate
        fields = ('mezun_yili', 'mezun_bolum', 'mezun_derece',)




    






