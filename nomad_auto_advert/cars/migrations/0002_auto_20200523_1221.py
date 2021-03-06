# Generated by Django 2.2.5 on 2020-05-23 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0002_cardrivetype_carenginetype_cartransmissiontype'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='drive_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drive_types', to='filters.CarDriveType'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='engine_types', to='filters.CarEngineType'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transmission_types', to='filters.CarTransmissionType'),
        ),
    ]
