# Generated by Django 4.2.1 on 2023-07-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
