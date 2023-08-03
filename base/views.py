from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import Graduate , Message, Event, FollowersAccount, Person, Location
from .forms import RegistrationForm,  UserUpdateForm, ProfileUpdateForm, FormWithCaptcha
from .tokens import account_activation_token
from django.http import Http404
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
import uuid
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def index(request):
    lisans_mezun_sayisi = Graduate.objects.filter(lisans=True).count()
    on_lisans_mezun_sayisi = Graduate.objects.filter(on_lisans=True).count()
    yuksek_lisans_mezun_sayisi = Graduate.objects.filter(yuksek_lisans=True).count()

    context = {
        'lisans_mezun_sayisi': lisans_mezun_sayisi,
        'on_lisans_mezun_sayisi': on_lisans_mezun_sayisi,
        'yuksek_lisans_mezun_sayisi': yuksek_lisans_mezun_sayisi,
    }
    return render(request, 'index.html', context)


def user_not_authenticated(user):
    return not user.is_authenticated


def loginPage(request): 
    if request.method == 'POST':
        form = FormWithCaptcha(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('captcha', False):
                messages.success(request, 'Giriş başarılı.')
        else:
            messages.error(request, 'Yanlış Captcha.')
            return redirect('login')
        tc_kimlik_no = request.POST.get('tc_kimlik_no')
        password = request.POST.get('password')
        

        try:
            user = Person.objects.get(tc_kimlik_no=tc_kimlik_no)

        except:
            messages.error(request, 'Girdiğiniz bilgiler hatalı.')


        user = authenticate(request, tc_kimlik_no=tc_kimlik_no, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş başarılı.')
            return render(request, 'anasayfa.html')
        else:
            messages.error(request, 'Girdiğiniz bilgiler hatalı.')
            return redirect('login')
    form = FormWithCaptcha()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = Person.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        # Kullanıcı aktif edilir
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Hesabınız başarıyla aktifleştirildi.')
        return redirect('login')  
    else:
        messages.error(request, 'Aktivasyon linki geçersiz.')
    return redirect('anasayfa')

def activateEmail(request, email):
    mail_subject = 'Hesabınızı aktive edin.'
    message = render_to_string('activate_account.html', {
        'user': request.user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(request.user.pk)),
        'token': account_activation_token.make_token(request.user),
        'protocol': 'https' if request.is_secure() else 'http',
    })
    email = EmailMessage(mail_subject, message, to=[email])
    if email.send():
        messages.success(request, f'Email adresinize bir aktivasyon linki gönderildi. Lütfen email adresinizi kontrol edin.')
    else:
        messages.error(request, f'Email adresinize gönderilemedi. Lütfen kontrol ediniz.')


def registerPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Şifreleme işlemi
            user.save()

            email = form.cleaned_data.get('email').lower()
            tc_kimlik_no = form.cleaned_data.get('tc_kimlik_no')

            account = authenticate(request, tc_kimlik_no=tc_kimlik_no, password=form.cleaned_data['password1'])
            if account is not None:
                messages.success(request, 'Hesabınız oluşturuldu.')
                login(request, account)
                activateEmail(request, email)
                return redirect('login')
            else:
                messages.error(request, 'Hatalı giriş veya eksik bilgi girdiniz.')

    else:
        form = RegistrationForm()

    context = {'registration_form': form}
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def anasayfa_view(request):
    return render(request, 'anasayfa.html')


def profile(request):
    user_id = request.user.id

    current_user = request.GET.get('user')
    locations = Location.objects.all()


    try:
        user_profile = Person.objects.get(id=user_id)
        graduate_profile = Graduate.objects.get(person=user_profile)
    except Person.DoesNotExist:
        user_profile = None
        graduate_profile = None
    except Graduate.DoesNotExist:
        graduate_profile = None

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi.')
            return redirect('profile')  # Profil sayfasına yönlendirme

        else:
            messages.error(request, 'Profiliniz güncellenemedi.')

    else:
        user_form = UserUpdateForm(instance=request.user) 
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)


    context = {'user_profile': user_profile,
            'current_user': current_user,
            'graduate_profile': graduate_profile,
            'user_form': user_form,
            'locations': locations,
            }

    return render(request, 'profile.html', context)


def view_profile(request, username):
    username = request.GET.get('username')
    if username:
        try:
            profile = Person.objects.get(username=username)
        except Person.DoesNotExist:
            profile = None
    try:
        # Query the user's data from the Person model
        user_profile = get_object_or_404(Person, username=username)

        # Assuming you have a 'Graduate' model for each user's graduation information
        try:
            graduate_profile = Graduate.objects.get(person=user_profile)
        except Graduate.DoesNotExist:
            graduate_profile = None

        # Rest of your code for the view_other_profile...

        context = {
            'user_profile': user_profile,
            'graduate_profile': graduate_profile,
            'profile' : profile,
        }

        return render(request, 'view_profile.html', context)

    except Http404:
        # If no user is found with the given username, render an error page
        return render(request, 'user_not_found.html')


def etkinlikler(request):
    etkinlikler = Event.objects.all()
    return render(request, 'etkinlikler.html', {'etkinlikler': etkinlikler})


def etkinlik_detay(request, pk):
    etkinlik = Event.objects.get(pk=pk)
    context = {
        'etkinlik': etkinlik
    }
    return render(request, 'etkinlik_detay.html', context)


def followers_count(request):
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        if value == 'follow':
            followers_cnt = FollowersAccount.objects.create(user=user, follower=follower)
            followers_cnt.save()
        else:
            followers_cnt = FollowersAccount.objects.get(user=user, follower=follower)
            followers_cnt.delete()
        return redirect('/?user='+user)


"""def save_changes(request):
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
    
    return render(request, 'guncelle.html', {'form': form})"""


def chat(request):
    messages = Message.objects.all()
    return render(request, 'header.html', {'messages': messages})   