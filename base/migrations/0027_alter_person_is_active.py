# Generated by Django 4.2.3 on 2023-08-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_person_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]