# Generated by Django 4.2.3 on 2023-07-28 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rename_universite_name_university_universite_adi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='universite_adi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university'),
        ),
    ]
