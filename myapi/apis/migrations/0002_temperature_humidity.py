# Generated by Django 4.0.2 on 2022-03-12 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.device')),
            ],
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.IntegerField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.device')),
            ],
        ),
    ]
