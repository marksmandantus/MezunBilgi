from django import forms
from django.core.validators import RegexValidator


class kaydet(forms.Form):
    email = forms.CharField(max_length=40)
    telefon = forms.CharField(max_length=11)
    adres = forms.CharField(max_length=70)

    # Diğer alanlar


class RegistrationForm(forms.Form):
    tc_kimlik_no = forms.IntegerField(
        label='TC Kimlik No',
        validators=[
            RegexValidator(
                regex='^[0-9]*$',
                message='TC Kimlik No sadece rakamlardan oluşmalıdır.',
                code='invalid_tc_kimlik_no'
            ),
        ]
    )
