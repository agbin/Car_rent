# Generated by Django 2.2.5 on 2019-09-09 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0010_auto_20190909_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='distance_in_km',
            new_name='how_many_days',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='price_for_km',
            new_name='price_for_one_day',
        ),
    ]
