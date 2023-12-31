# Generated by Django 4.2.1 on 2023-07-21 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ad', models.CharField(max_length=50)),
                ('soyad', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, null=True, unique=True)),
                ('telefon', models.CharField(max_length=50, null=True, unique=True)),
                ('adres', models.CharField(max_length=50, null=True, unique=True)),
                ('profil', models.ImageField(blank=True, null=True, upload_to='profil/')),
                ('tc_kimlik_no', models.CharField(max_length=50, null=True, unique=True)),
                ('cinsiyet', models.CharField(max_length=50, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etkinlik_adi', models.CharField(max_length=50)),
                ('etkinlik_tarihi', models.DateField()),
                ('etkinlik_yeri', models.CharField(max_length=50)),
                ('etkinlik_suresi', models.CharField(max_length=50)),
                ('etkinlik_katilimcisi', models.CharField(max_length=50)),
                ('etkinlik_icerigi', models.TextField()),
                ('etkinlik_resim', models.FileField(blank=True, null=True, upload_to='')),
                ('etkinlik_video', models.FileField(blank=True, null=True, upload_to='')),
                ('etkinlik_dosya', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FollowersAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=1000)),
                ('user', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Graduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mezun_yili', models.IntegerField()),
                ('mezun_bolum', models.CharField(max_length=50)),
                ('mezun_derece', models.CharField(max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.graduate')),
            ],
        ),
    ]
