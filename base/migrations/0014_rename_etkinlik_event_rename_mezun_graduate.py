# Generated by Django 4.2.1 on 2023-07-19 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_rename_event_etkinlik_rename_graduate_mezun'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Etkinlik',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Mezun',
            new_name='Graduate',
        ),
    ]