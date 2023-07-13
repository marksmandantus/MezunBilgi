from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect 
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Mezun , Mesaj


# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
             messages.error(request, 'Email veya şifre hatalı')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'anasayfa.html')
        else:
            messages.error(request, 'Email veya şifre hatalı')
            return render(request, 'login.html')

    return render(request, 'login.html')


def profile(request):
    user = Mezun.objects.all()
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/login/')
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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Kullanıcı kaydolduktan sonra yönlendirileceği sayfa
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})