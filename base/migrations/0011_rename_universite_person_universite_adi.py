# Generated by Django 4.2.1 on 2023-07-24 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_ad_universite_universite_adi_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='universite',
            new_name='universite_adi',
        ),
    ]
