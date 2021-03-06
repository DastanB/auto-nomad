# Generated by Django 2.2.5 on 2020-08-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0013_auto_20200824_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='id_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='advert',
            name='id_hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='advert',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='advert',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'created'), (2, 'moderation'), (3, 'active'), (4, 'blocked')], default=1),
        ),
    ]
