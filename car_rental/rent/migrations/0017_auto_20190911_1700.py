# Generated by Django 2.2.5 on 2019-09-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0016_auto_20190910_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price_for_a_day',
            field=models.IntegerField(),
        ),
    ]
