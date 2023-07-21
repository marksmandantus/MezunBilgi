from django.db import models
from django.contrib.auth.models import User


class Graduate(models.Model):
    id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    mezun_yili = models.IntegerField()
    mezun_bolum = models.CharField(max_length=50)
    mezun_derece = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, unique=True)
    sifre = models.CharField(max_length=50, null=True)
    cinsiyet = models.CharField(max_length=50, null=True)
    telefon = models.CharField(max_length=50, null=True, unique=True)
    adres = models.CharField(max_length=50, unique=True, null=True)
    profil = models.ImageField(null=True, blank=True, upload_to="profil/")
    tc_kimlik_no = models.CharField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.ad + ' ' + self.soyad
    

class FollowersAccount(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user
        

class Message(models.Model):
    user = models.ForeignKey(Graduate, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]



class Event(models.Model):
    id: models.AutoField(primary_key=True)
    etkinlik_adi = models.CharField(max_length=50)
    etkinlik_tarihi = models.DateField()
    etkinlik_yeri = models.CharField(max_length=50)
    etkinlik_suresi = models.CharField(max_length=50)
    etkinlik_katilimcisi = models.CharField(max_length=50)
    etkinlik_icerigi = models.TextField()
    etkinlik_resim = models.FileField(null=True, blank=True)
    etkinlik_video = models.FileField(null=True, blank=True)
    etkinlik_dosya = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.etkinlik_adi



