# Generated by Django 4.0.6 on 2022-08-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='result',
            new_name='measurements',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
