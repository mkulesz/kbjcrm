# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kbjcrm', '0011_auto_20170421_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='Rola',
            field=models.ForeignKey(default='Osoba', on_delete=django.db.models.deletion.CASCADE, to='kbjcrm.Rola'),
        ),
    ]
