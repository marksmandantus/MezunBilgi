from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Graduate , Message, Event, FollowersAccount, Person
from .forms import kaydet 
from .forms import RegistrationForm, GraduateForm
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def view_profile(request, username):
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
        }

        return render(request, 'view_profile.html', context)

    except Http404:
        # If no user is found with the given username, render an error page
        return render(request, 'user_not_found.html')

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    context = {}
    if request.method == 'POST':
        tc_kimlik_no = request.POST.get('tc_kimlik_no')
        password = request.POST.get('password')

        try:
            user = Person.objects.get(tc_kimlik_no=tc_kimlik_no)

        except:
            context['error_message'] = 'Kullanıcı adı veya şifre hatalı'


        user = authenticate(request, tc_kimlik_no=tc_kimlik_no, password=password)

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

    current_user = request.GET.get('user')
    # logged_in_user = request.user.username(email)

    # Query the logged-in user's data from the Graduate model
    try:
        user_profile = Person.objects.get(id=user_id)
        graduate_profile = Graduate.objects.get(person=user_profile)
    except Person.DoesNotExist:
        user_profile = None
        graduate_profile = None
    except Graduate.DoesNotExist:
        graduate_profile = None

    user_followers = len(FollowersAccount.objects.filter(user=current_user))
    user_following = len(FollowersAccount.objects.filter(follower=current_user))
    user_followers0 = FollowersAccount.objects.filter(user=current_user)
    user_followers1 = []

    for i in user_followers0:
        user_followers0 = i.follower
        user_followers1.append(user_followers0)

    """if logged_in_user in user_followers1:
        follow_button_value = 'unfollow'
    else:
        follow_button_value = 'follow'

    print(user_followers)"""

    context = {'user_profile': user_profile,
            'user_followers': user_followers,
            'user_following': user_following,
            #'follow_button_value': follow_button_value,
            'current_user': current_user,
            'graduate_profile': graduate_profile,}

    return render(request, 'profile.html', context)

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


def edit_profile(request):
     # Get the logged-in user's ID
    user_id = request.user.id

    # Query the logged-in user's data from the Graduate model
    try:
        user_profile = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        # Handle the case if the user doesn't exist in the database
        user_profile = None

    return render(request, 'guncelle.html', {'user_profile': user_profile})


def anasayfa_view(request):
    return render(request, 'anasayfa.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def etkinlikler(request):
    etkinlikler = Event.objects.all()

    return render(request, 'etkinlikler.html', {'etkinlikler': etkinlikler})


def etkinlik_detay(request, pk):
    etkinlik = Event.objects.get(pk=pk)
    context = {
        'etkinlik': etkinlik
    }
    return render(request, 'etkinlik_detay.html', context)

def user_not_authenticated(user):
    return not user.is_authenticated

def registerPage(request, *args, **kwargs):
    context = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        graduate_form = GraduateForm(request.POST)
        if form.is_valid() and graduate_form.is_valid():
            user = form.save(commit=False)  # Save the user form without committing to the database
            user.save()  # Now, save the user to the database

            graduate = graduate_form.save(commit=False)  # Save the graduate form without committing to the database
            graduate.person = user  # Set the 'person' field to the newly created user
            graduate.save()  # Now, save the graduate to the database
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            tc_kimlik_no = form.cleaned_data.get('tc_kimlik_no')
            ad = form.cleaned_data.get('ad')
            soyad = form.cleaned_data.get('soyad')
            telefon = form.cleaned_data.get('telefon')
            username = form.cleaned_data.get('username')
            mezun_yili = graduate_form.cleaned_data.get('mezun_yili')
            mezun_bolum = graduate_form.cleaned_data.get('mezun_bolum')
            mezun_derece = graduate_form.cleaned_data.get('mezun_derece')
            account = authenticate(email=email, password=raw_password, tc_kimlik_no=tc_kimlik_no, ad=ad, soyad=soyad, telefon=telefon, username=username,
                                   mezun_yili=mezun_yili, mezun_bolum=mezun_bolum, mezun_derece=mezun_derece)
            login(request,account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect('login')
        else:
            context['registration_form'] = form

    return render(request, 'register.html', context)


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


def chat(request):
    messages = Message.objects.all()
    return render(request, 'header.html', {'messages': messages})   