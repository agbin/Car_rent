# Generated by Django 2.2.5 on 2019-09-11 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0020_auto_20190911_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='lender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='rent.Lender'),
        ),
    ]