# Generated by Django 2.0.13 on 2020-04-07 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_ext', models.PositiveIntegerField()),
                ('car_condition_type', models.IntegerField(blank=True, choices=[(0, 'Новый'), (1, 'На ходу'), (2, 'Не на ходу'), (3, 'Аварийная')], null=True)),
                ('cleared_by_customs', models.BooleanField(default=False)),
                ('city_ext', models.PositiveIntegerField(blank=True, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=1, max_digits=99)),
                ('exchange', models.BooleanField(default=False)),
                ('to_order', models.BooleanField(default=False)),
                ('rule_type', models.IntegerField(blank=True, choices=[(0, 'Справа'), (1, 'Слева')], default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertContactPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advert_phones', to='advert.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('advert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advert_images', to='advert.Advert')),
            ],
        ),
    ]
