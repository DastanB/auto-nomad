# Generated by Django 2.2.5 on 2020-08-23 18:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_contactphone'),
        ('advert', '0011_advert_contact_phones'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', models.TextField()),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='advert.Advert')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='advert.AdvertComment')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]