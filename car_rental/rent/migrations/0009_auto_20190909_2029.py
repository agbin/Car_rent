# Generated by Django 2.2.5 on 2019-09-09 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0008_auto_20190909_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='distance',
            new_name='distance_km',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='price',
            new_name='price_for_km',
        ),
    ]
