# Generated by Django 2.2.5 on 2019-09-09 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_auto_20190909_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='lender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case', to='rent.Lender'),
        ),
    ]