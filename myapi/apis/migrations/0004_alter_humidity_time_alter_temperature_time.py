# Generated by Django 4.0.2 on 2022-03-12 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_humidity_time_temperature_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 11, 34, 43, 831285)),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 11, 34, 43, 830956)),
        ),
    ]
