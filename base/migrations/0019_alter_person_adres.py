# Generated by Django 4.2.3 on 2023-07-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_person_universite_adi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='adres',
            field=models.CharField(max_length=200, null=True),
        ),
    ]