# Generated by Django 4.2.3 on 2023-08-01 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_person_facebook_alter_person_github_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='facebook',
        ),
    ]
