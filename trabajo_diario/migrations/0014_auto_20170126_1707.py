# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-26 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabajo_diario', '0013_auto_20170126_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tareadiaria',
            name='mi_dia',
        ),
        migrations.RemoveField(
            model_name='trabajodia',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='TareaDiaria',
        ),
        migrations.DeleteModel(
            name='TrabajoDia',
        ),
    ]