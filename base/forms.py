from django import forms

class kaydet(forms.Form):
    email = forms.CharField(max_length=40)
    telefon = forms.CharField(max_length=11)
    adres = forms.CharField(max_length=70)

    # Diğer alanlar
