# Generated by Django 2.2.5 on 2020-05-25 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_volume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='volume',
            new_name='engine_volume',
        ),
    ]
