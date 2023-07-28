import factory
from django.contrib.auth.models import User
from .models import University , Event, Person, Graduate
from faker import Faker


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event
        django_get_or_create = ('etkinlik_adi', 'etkinlik_tarihi', 'etkinlik_yeri', 'etkinlik_suresi', 'etkinlik_icerigi', 'etkinlik_katilimcisi', 'etkinlik_resim')

    etkinlik_adi = factory.Faker('company')
    etkinlik_tarihi = factory.Faker('date')
    etkinlik_yeri = factory.Faker('city')
    etkinlik_suresi = factory.Faker('pyint')
    etkinlik_icerigi = factory.Faker('sentence')
    etkinlik_katilimcisi = factory.Faker('name')
    etkinlik_resim = factory.Faker('image_url')


class UniversityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = University

    universite_adi = factory.Faker('company')
    sehir = factory.Faker('city')
    kurulus_yili = factory.Faker('year')
    web_site = factory.Faker('url')
    logo = factory.django.ImageField()
    universite_adres = factory.Faker('address')
    universite_telefon = factory.Faker('phone_number')
    universite_eposta = factory.Faker('email')
    fax = factory.Faker('phone_number')
    rektor = factory.Faker('name')
    genel_sekreter = factory.Faker('name')
    baskan = factory.Faker('name')
    profesor_sayisi = factory.Faker('pyint')
    docent_sayisi = factory.Faker('pyint')
    ogretim_gorevlisi_sayisi = factory.Faker('pyint')
    arastirma_gorevlisi_sayisi = factory.Faker('pyint')
    ogrenci_sayisi = factory.Faker('pyint')
    lisans_program_sayisi = factory.Faker('pyint')
    on_lisans_program_sayisi = factory.Faker('pyint')
    yuksek_lisans_program_sayisi = factory.Faker('pyint')


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    ad = factory.Faker('first_name')
    username = factory.Faker('user_name')
    soyad = factory.Faker('last_name')
    email = factory.Faker('email')
    telefon = factory.Faker('phone_number')
    adres = factory.Faker('address')
    profil = factory.django.ImageField()
    tc_kimlik_no = factory.Faker('ssn')
    cinsiyet = factory.Faker('random_element', elements=('Erkek', 'Kadın'))
    dogum_tarihi = factory.Faker('date_of_birth')
    universite_adi = factory.SubFactory(UniversityFactory)
    website = factory.Faker('url')
    facebook = factory.Faker('url')
    twitter = factory.Faker('url')
    instagram = factory.Faker('url')
    linkedin = factory.Faker('url')
    github = factory.Faker('url')
    is_admin = factory.Faker('boolean')
    is_active = True
    is_staff = factory.Faker('boolean')
    is_superuser = False


class GraduateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Graduate

    person = factory.SubFactory(PersonFactory)
    mezun_yili = factory.Faker('pyint', min_value=2000, max_value=2023)
    mezun_bolum = factory.Faker('word')
    mezun_derece = factory.Faker('pyint')
    lisans = factory.Faker('boolean')
    on_lisans = factory.Faker('boolean')
    yuksek_lisans = factory.Faker('boolean')