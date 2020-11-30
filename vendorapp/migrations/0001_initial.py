# Generated by Django 2.2.6 on 2020-11-29 19:24

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=90, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=40)),
                ('mobile_number', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=40)),
                ('address_2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
