# Generated by Django 4.2.1 on 2023-07-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_person_dogum_tarihi_person_facebook_person_github_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='lisans',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='on_lisans',
            field=models.BooleanField(default=False),
        ),
    ]