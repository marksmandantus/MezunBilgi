from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profil/,', views.edit_profil, name='edit_profil'),
    path('anasayfa/', views.anasayfa_view, name='anasayfa'),
    path('logout/', views.logout_view, name='logout'),
    path('is-ilanlari/', views.is_ilanlari, name='is_ilanlari'),
    path('etkinlikler/', views.etkinlikler, name='etkinlikler'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]