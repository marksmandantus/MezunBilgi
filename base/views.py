from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Mezun , Mesaj


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
    return render(request, 'edit_profile.html')