# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbjcrm', '0004_kontrahent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrahent',
            name='IdKontrahent',
            field=models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='IdOsoba',
            field=models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False),
        ),
    ]
