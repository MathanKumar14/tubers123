# Generated by Django 3.1.5 on 2021-04-18 10:31

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('webpages', '0003_auto_20210418_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('fb_link', models.CharField(max_length=955)),
                ('insta_link', models.CharField(max_length=955)),
                ('twitter_link', models.CharField(max_length=955)),
                ('youtuber_link', models.CharField(max_length=955)),
                ('address', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
    ]