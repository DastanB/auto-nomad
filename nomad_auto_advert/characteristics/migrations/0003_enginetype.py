# Generated by Django 2.0.13 on 2020-04-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0002_carbodytype'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
