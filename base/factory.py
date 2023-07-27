import factory
from django.contrib.auth.models import User
from .models import University , Event
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