# Generated by Django 4.2.3 on 2023-07-14 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_mezun_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mezun',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='mezun',
            name='password',
        ),
    ]