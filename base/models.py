from django.db import models


class Mezun(models.Model):
    id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    mezun_yili = models.IntegerField()
    mezun_bolum = models.CharField(max_length=50)
    mezun_derece = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    sifre = models.CharField(max_length=50, null=True)
    cinsiyet = models.CharField(max_length=50, null=True)
    telefon = models.CharField(max_length=50, null=True)
    adres = models.CharField(max_length=50, unique=True, null=True)
    profil = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.ad + ' ' + self.soyad
    

class Mesaj(models.Model):
    mezun = models.ForeignKey(Mezun, on_delete=models.CASCADE)
    icerik = models.TextField()




