# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbjcrm', '0005_auto_20170421_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='IdOsoba',
            field=models.CharField(auto_created=True, editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
