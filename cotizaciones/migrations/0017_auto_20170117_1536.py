# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0016_cotizacion_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='version',
            field=models.PositiveIntegerField(default=1),
        ),
    ]