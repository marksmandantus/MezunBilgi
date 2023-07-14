from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adı'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-posta'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifre'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifre tekrarı'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
