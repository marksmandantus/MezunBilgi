from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin


class University(models.Model):
    universite_adi = models.CharField(max_length=100)
    sehir = models.CharField(max_length=100)
    kurulus_yili = models.PositiveIntegerField()
    web_site = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True, upload_to="logo/")
    universite_adres = models.CharField(max_length=100)
    universite_telefon = models.CharField(max_length=100)
    universite_eposta = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    rektor = models.CharField(max_length=100)
    genel_sekreter = models.CharField(max_length=100)
    baskan = models.CharField(max_length=100)
    profesor_sayisi = models.PositiveIntegerField()
    docent_sayisi = models.PositiveIntegerField()
    ogretim_gorevlisi_sayisi = models.PositiveIntegerField()
    arastirma_gorevlisi_sayisi = models.PositiveIntegerField()
    ogrenci_sayisi = models.PositiveIntegerField()
    lisans_program_sayisi = models.PositiveIntegerField()
    on_lisans_program_sayisi = models.PositiveIntegerField()
    yuksek_lisans_program_sayisi = models.PositiveIntegerField()

    def __str__(self):
        return self.universite_adi
    

class Location(models.Model):
    sehir = models.CharField(max_length=50)

    def __str__(self):
        return self.sehir 
    

class PersonManager(BaseUserManager):
    
    def create_user(self,tc_kimlik_no,username, password=None, ):
        if not tc_kimlik_no:
            raise ValueError("TC kimlik numarası boş bırakılamaz!")
        
        user = self.model(
            tc_kimlik_no = tc_kimlik_no,
            username = username,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,tc_kimlik_no,password, username):
        user = self.create_user(
            tc_kimlik_no = tc_kimlik_no,
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Person(AbstractBaseUser, PermissionsMixin):
    ad = models.CharField(max_length=50)
    username = models.CharField(max_length=50, null=True, unique=True)
    soyad = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, unique=True)
    telefon = models.CharField(max_length=50, null=True, unique=True)
    adres = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    profil = models.ImageField(null=True, blank=True, upload_to="profil/")
    tc_kimlik_no = models.CharField(max_length=11, null=True, unique=True)
    cinsiyet = models.CharField(max_length=50, null=True)
    dogum_tarihi = models.DateField(null=True)
    website = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=50, null=True)
    facebook = models.CharField(max_length=50, null=True)
    instagram = models.CharField(max_length=50, null=True)
    linkedin = models.CharField(max_length=50, null=True)
    github = models.CharField(max_length=50, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = PersonManager()

    USERNAME_FIELD = 'tc_kimlik_no'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.ad + ' ' + self.soyad
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    


class Graduate(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    mezun_yili = models.IntegerField()
    mezun_bolum = models.CharField(max_length=50)
    mezun_derece = models.PositiveIntegerField()
    lisans = models.BooleanField(default=False)
    on_lisans = models.BooleanField(default=False)
    yuksek_lisans = models.BooleanField(default=False)
    universite_adi = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.person.ad + ' ' + self.person.soyad
    

class FollowersAccount(models.Model):
    follower = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='followers')
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='following')


    def __str__(self):
        return self.user
        

class Message(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]



class Event(models.Model):
    id = models.AutoField(primary_key=True)
    mezunlar = models.ManyToManyField(Graduate, blank=True, related_name='etkinlikler')
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



