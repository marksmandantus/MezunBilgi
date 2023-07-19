from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Graduate , Mesaj, Event
from .forms import kaydet , CustomUserCreationForm



# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Graduate.objects.get(username=username)

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
    # Get the logged-in user's ID
    user_id = request.user.id

    # Query the logged-in user's data from the Graduate model
    try:
        user_profile = Graduate.objects.get(id=user_id)
    except Graduate.DoesNotExist:
        # Handle the case if the user doesn't exist in the database
        user_profile = None

    return render(request, 'profile.html', {'user_profile': user_profile})


def edit_profile(request):
     # Get the logged-in user's ID
    user_id = request.user.id

    # Query the logged-in user's data from the Graduate model
    try:
        user_profile = Graduate.objects.get(id=user_id)
    except Graduate.DoesNotExist:
        # Handle the case if the user doesn't exist in the database
        user_profile = None

    return render(request, 'guncelle.html', {'user_profile': user_profile})


def anasayfa_view(request):
    return render(request, 'anasayfa.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def is_ilanlari(request):
    return render(request, 'is_ilanlari.html')

def etkinlikler(request):
    etkinlikler = Event.objects.all()

    return render(request, 'etkinlikler.html', {'etkinlikler': etkinlikler})


def etkinlik_detay(request, pk):
    etkinlik = Event.objects.get(pk=pk)
    context = {
        'etkinlik': etkinlik
    }
    return render(request, 'etkinlik_detay.html', context)

def registerPage(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Hesabınız oluşturuldu')
            return redirect('login')
        
        else:
            messages.error(request, 'Hesabınız oluşturulamadı')

    return render(request, 'register.html', {'form': form})


def save_changes(request):
    if request.method == 'POST':
        form = kaydet(request.POST)
        if form.is_valid():
            # Form verilerini kaydetme işlemini burada gerçekleştirin
            email = request.POST.get('email')
            telefon = request.POST.get('telefon')
            adres = request.POST.get('adres')

            Graduate = Graduate.objects.get(id=request.user.id)

            Graduate.email = email
            Graduate.telefon = telefon
            Graduate.adres = adres

            Graduate.save()
           
            return redirect('profile')
    else:
        form = kaydet()
    
    return render(request, 'guncelle.html', {'form': form})