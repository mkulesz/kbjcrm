# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 14:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kbjcrm', '0014_auto_20170424_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='naleznosc',
            old_name='Data',
            new_name='Data_platnosci',
        ),
        migrations.RenameField(
            model_name='naleznosc',
            old_name='Kwota',
            new_name='Kwota_oplaty',
        ),
        migrations.RemoveField(
            model_name='kontrakt',
            name='Data_platnosci_fizycznej',
        ),
        migrations.RemoveField(
            model_name='kontrakt',
            name='Kwota_oplaty_licencyjnej',
        ),
    ]