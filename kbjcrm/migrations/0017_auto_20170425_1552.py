# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbjcrm', '0016_auto_20170425_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naleznosc',
            name='Zrealizowane',
            field=models.BooleanField(default=False),
        ),
    ]
