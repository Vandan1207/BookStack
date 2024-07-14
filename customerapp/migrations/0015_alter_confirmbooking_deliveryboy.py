# Generated by Django 5.0.1 on 2024-04-17 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_deliveryboy_is_registered'),
        ('customerapp', '0014_confirmbooking_deliveryboy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmbooking',
            name='deliveryboy',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.CASCADE, to='adminapp.deliveryboy'),
            preserve_default=False,
        ),
    ]
