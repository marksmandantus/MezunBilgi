from django.contrib import admin
from .models import Graduate, Event

class GraduateAdmin(admin.ModelAdmin):
    list_display = ('ad','soyad','mezun_bolum','mezun_yili','telefon','tc')
    list_filter = ('mezun_yili','mezun_bolum','ad','soyad','tc')
    ordering = ('mezun_yili',)
    search_fields = ('mezun_yili','mezun_bolum','ad','soyad','tc',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('etkinlik_adi',)
    list_filter = ('etkinlik_adi',)
    search_fields = ('etkinlik_adi',)

admin.site.register(Graduate, GraduateAdmin)
admin.site.register(Event,EventAdmin)


admin.site.site_title = 'Mezun Bilgi Sistemi'
admin.site.site_header = 'Mezun Bilgi Sistemi' # Login ekranında da gözükür.

admin.site.index_title = 'Mezun Bilgi Sistemine Hoşgeldiniz.'



