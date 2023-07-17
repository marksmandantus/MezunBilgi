from django.contrib import admin
from .models import Mezun , Etkinlikler

admin.site.register(Mezun)
admin.site.register(Etkinlikler)

admin.site.site_title = 'Mezun Bilgi Sistemi'

admin.site.site_header = 'Mezun Bilgi Sistemi'

admin.site.index_title = 'Mezun Bilgi Sistemine Hoşgeldiniz.'



