# Generated by Django 4.2.3 on 2023-07-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_mezun_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='mezun',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
