# Generated by Django 5.0.1 on 2024-07-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_deliveryboy_is_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='Author',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
