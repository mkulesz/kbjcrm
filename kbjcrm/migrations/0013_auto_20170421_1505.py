# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kbjcrm', '0012_osoba_rola'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='Rola',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbjcrm.Rola'),
        ),
    ]