# Generated by Django 2.2.5 on 2020-08-11 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200723_1129'),
        ('cars', '0014_option_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='users.Profile'),
        ),
    ]
