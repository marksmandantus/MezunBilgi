# Generated by Django 4.2.3 on 2023-07-26 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rename_universite_adi_university_universite_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='universite_name',
            new_name='universite_adi',
        ),
    ]