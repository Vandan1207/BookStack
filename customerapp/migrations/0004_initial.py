# Generated by Django 5.0.1 on 2024-02-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customerapp', '0003_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('emial', models.EmailField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('city', models.TextField()),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
