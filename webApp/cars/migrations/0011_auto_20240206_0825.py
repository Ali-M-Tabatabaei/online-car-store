# Generated by Django 3.0.7 on 2024-02-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20240206_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
