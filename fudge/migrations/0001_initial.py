# Generated by Django 4.2.16 on 2024-09-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_company', models.CharField(max_length=200)),
                ('bus_number', models.CharField(max_length=5)),
                ('bus_stop', models.CharField(max_length=300)),
                ('bus_time', models.TimeField()),
            ],
        ),
    ]