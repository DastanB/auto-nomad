# Generated by Django 2.0.13 on 2020-04-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBodyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
