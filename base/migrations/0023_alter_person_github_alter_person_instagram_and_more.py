# Generated by Django 4.2.3 on 2023-08-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_remove_person_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='github',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='instagram',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='twitter',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='website',
            field=models.CharField(max_length=50, null=True),
        ),
    ]