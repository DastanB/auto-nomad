# Generated by Django 2.2.5 on 2020-08-27 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200827_1158'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contactphone',
            unique_together={('profile', 'phone')},
        ),
    ]