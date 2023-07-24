from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Graduate, Event, Message, FollowersAccount, Person, University

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('universite_adi',)
    list_filter = ('universite_adi',)
    search_fields = ('universite_adi',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('ad', 'soyad', 'email', 'username', 'telefon', 'adres', 'tc_kimlik_no','cinsiyet', 'profil', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('ad','soyad','tc_kimlik_no', 'username')
    list_display_links = ('ad', 'soyad', 'tc_kimlik_no', 'username')  # Bu alanlar üzerine tıklandığında düzenleme ekranı açılacak
    ordering = ('ad',)
    search_fields = ('tc_kimlik_no',)


class GraduateAdmin(admin.ModelAdmin):
    list_display = ('mezun_yili', 'mezun_bolum', 'mezun_derece')
    list_filter = ('mezun_yili','mezun_bolum')
    ordering = ('mezun_yili',)
    search_fields = ('mezun_yili','mezun_bolum',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('etkinlik_adi',)
    list_filter = ('etkinlik_adi',)
    search_fields = ('etkinlik_adi',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created', 'updated')
    list_filter = ('user', 'created', 'updated')
    search_fields = ('user','body',)

admin.site.register(Graduate, GraduateAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(University,UniversityAdmin)
admin.site.register(FollowersAccount)


admin.site.site_title = 'Mezun Bilgi Sistemi'
admin.site.site_header = 'Mezun Bilgi Sistemi' # Login ekranında da gözükür.

admin.site.index_title = 'Mezun Bilgi Sistemine Hoşgeldiniz.'



