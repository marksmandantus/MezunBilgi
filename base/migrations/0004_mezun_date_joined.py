# Generated by Django 4.2.3 on 2023-07-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_mezun_last_login_mezun_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='mezun',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
