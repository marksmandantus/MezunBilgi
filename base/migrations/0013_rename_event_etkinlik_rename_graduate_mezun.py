# Generated by Django 4.2.1 on 2023-07-19 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_rename_etkinlikler_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Etkinlik',
        ),
        migrations.RenameModel(
            old_name='Graduate',
            new_name='Mezun',
        ),
    ]