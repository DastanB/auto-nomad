# Generated by Django 2.2.5 on 2020-08-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_auto_20200812_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmark',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
