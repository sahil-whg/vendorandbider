# Generated by Django 2.2.6 on 2020-11-29 19:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0004_auto_20201130_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
