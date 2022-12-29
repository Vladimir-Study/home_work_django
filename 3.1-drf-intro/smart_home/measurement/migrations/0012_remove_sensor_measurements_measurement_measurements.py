# Generated by Django 4.0.6 on 2022-08-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0011_alter_sensor_measurements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='measurements',
        ),
        migrations.AddField(
            model_name='measurement',
            name='measurements',
            field=models.ManyToManyField(blank=True, null=True, related_name='measurements', to='measurement.sensor', verbose_name='Измерения'),
        ),
    ]