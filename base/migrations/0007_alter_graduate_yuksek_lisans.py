# Generated by Django 4.2.1 on 2023-07-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_graduate_lisans_alter_graduate_on_lisans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='yuksek_lisans',
            field=models.BooleanField(default=False),
        ),
    ]