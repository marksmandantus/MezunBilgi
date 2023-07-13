from django.contrib import admin
from .models import Mezun , CustomUser

admin.site.register(Mezun)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_approved']
    list_filter = ['is_approved']

admin.site.register(CustomUser, CustomUserAdmin)

