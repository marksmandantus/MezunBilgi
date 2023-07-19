from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class kaydet(forms.Form):
    email = forms.CharField(max_length=40)
    telefon = forms.CharField(max_length=11)
    adres = forms.CharField(max_length=70)

    # Diğer alanlar


class CustomUserCreationForm(UserCreationForm):
    tc_kimlik_no = forms.CharField(
        label='TC Kimlik No',
        validators=[
            RegexValidator(
                regex='^[0-9]{11}$',
                message='TC Kimlik No sadece rakamlardan oluşmalıdır.',
                code='invalid_tc_kimlik_no'
            ),
        ]
    )

    password1 = forms.CharField(
        label='Şifre',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Şifre Tekrar',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor.")
        return password2

    class Meta:
        model = User  # User modelini buraya ekleyin
        fields = ('tc_kimlik_no', 'password1', 'password2')  # Diğer form alanlarını buraya ekleyin
