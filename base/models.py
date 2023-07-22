from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin

class PersonManager(BaseUserManager):
    
    def create_user(self,tc_kimlik_no,password=None):
        if not tc_kimlik_no:
            raise ValueError("TC kimlik numarası boş bırakılamaz!")
        
        user = self.model(
            tc_kimlik_no = tc_kimlik_no,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,tc_kimlik_no,password):
        user = self.create_user(
            tc_kimlik_no = tc_kimlik_no,
            password = password,
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
    adres = models.CharField(max_length=50, unique=True, null=True)
    profil = models.ImageField(null=True, blank=True, upload_to="profil/")
    tc_kimlik_no = models.CharField(max_length=50, null=True, unique=True)
    cinsiyet = models.CharField(max_length=50, null=True)
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
    mezun_derece = models.CharField(max_length=50)

    def __str__(self):
        return self.person.ad + ' ' + self.person.soyad
    

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



