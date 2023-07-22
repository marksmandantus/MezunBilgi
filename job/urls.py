from django.urls import path
from . import views

urlpatterns = [
    path('is-ilanlari/', views.is_ilanlari, name='is_ilanlari'),
    path('web-gelistirici/', views.web_gelistirici, name='web_gelistirici'), 
]