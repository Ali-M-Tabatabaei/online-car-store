# Generated by Django 3.0.7 on 2024-02-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20240206_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
