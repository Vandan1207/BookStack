# Generated by Django 5.0.1 on 2024-02-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0011_remove_confirmbooking_delivery_boy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
