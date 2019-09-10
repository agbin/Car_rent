# Generated by Django 2.2.5 on 2019-09-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lender',
            name='trip',
        ),
        migrations.AddField(
            model_name='trip',
            name='client_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='trip',
            name='lender',
            field=models.ManyToManyField(to='rent.Lender'),
        ),
    ]