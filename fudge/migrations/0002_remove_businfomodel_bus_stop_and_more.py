# Generated by Django 4.2.16 on 2024-09-27 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fudge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businfomodel',
            name='bus_stop',
        ),
        migrations.RemoveField(
            model_name='businfomodel',
            name='bus_time',
        ),
        migrations.CreateModel(
            name='BusStopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_stop', models.CharField(max_length=1000)),
                ('bus_time', models.TimeField()),
                ('bus_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='fudge.businfomodel')),
            ],
        ),
    ]