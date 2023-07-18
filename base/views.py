from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Mezun , Mesaj, Etkinlikler
from .forms import kaydet, RegistrationForm



# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Mezun.objects.get(username=username)

        except:
            context['error_message'] = 'Kullanıcı adı veya şifre hatalı'


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'anasayfa.html')
        else:
            context['error_message'] = 'Kullanıcı adı veya şifre hatalı'
            return redirect('login')
            
    return render(request, 'login.html', context)


def profile(request):
    mezunlar = Mezun.objects.all()
    context = {
        'mezunlar': mezunlar
    }
    return render(request, 'profile.html', context)


def anasayfa_view(request):
    kullanici = Mezun.objects.all()
    messages = Mesaj.objects.filter(mezun__in=kullanici)
    context = {
        'kullanici': kullanici,
        'messages': messages
    }
    
    return render(request, 'anasayfa.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def is_ilanlari(request):
    return render(request, 'is_ilanlari.html')

def etkinlikler(request):
    return render(request, 'etkinlikler.html')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Hesabınız oluşturuldu')
            return redirect('login')
        
        else:
            messages.error(request, 'Hesabınız oluşturulamadı')

    return render(request, 'register.html', {'form': form})


def edit_profile(request):
    mezunlar = Mezun.objects.all()
    context = {
        'mezunlar': mezunlar
    }
    return render(request, 'guncelle.html' , context)

def etkinlikler(request): 
    etkinlikler = Etkinlikler.objects.all()
    context = {
        'etkinlikler': etkinlikler,
    }
    return render(request, 'etkinlikler.html', context)


def etkinlik_detay(request, pk):
    etkinlik = Etkinlikler.objects.get(pk=pk)
    context = {
        'etkinlik': etkinlik
    }
    return render(request, 'etkinlik_detay.html', context)


def save_changes(request):
    if request.method == 'POST':
        form = kaydet(request.POST)
        if form.is_valid():
            # Form verilerini kaydetme işlemini burada gerçekleştirin
            email = request.POST.get('email')
            telefon = request.POST.get('telefon')
            adres = request.POST.get('adres')

            mezun = Mezun.objects.get(id=request.user.id)

            mezun.email = email
            mezun.telefon = telefon
            mezun.adres = adres

            mezun.save()
           
            return redirect('profile')
    else:
        form = kaydet()
    
    return render(request, 'guncelle.html', {'form': form})