# Generated by Django 2.2.5 on 2020-07-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_car_car_ext'),
    ]

    operations = [
        migrations.AddField(
            model_name='carcolor',
            name='ext',
            field=models.PositiveSmallIntegerField(null=True, unique=True),
        ),
    ]
