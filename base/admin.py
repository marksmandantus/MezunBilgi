from django.contrib import admin
from .models import Mezun

class MezunAdmin(admin.ModelAdmin):
    list_display = ('ad','soyad','mezun_bolum','mezun_yili','telefon','tc')
    list_filter = ('mezun_yili','mezun_bolum','ad','soyad','tc')
    ordering = ('mezun_yili',)
    search_fields = ('tc',)

admin.site.register(Mezun, MezunAdmin)


admin.site.site_title = 'Mezun Bilgi Sistemi'
admin.site.site_header = 'Mezun Bilgi Sistemi' # Login ekranında da gözükür.

admin.site.index_title = 'Mezun Bilgi Sistemine Hoşgeldiniz.'



