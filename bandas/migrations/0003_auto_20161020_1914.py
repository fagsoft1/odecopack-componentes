# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_remove_ensamblado_cortado_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ensamblado',
            name='ancho',
        ),
        migrations.AddField(
            model_name='ensamblado',
            name='cortado_a',
            field=models.CharField(default='HOLA', max_length=10, verbose_name='Cortado a'),
            preserve_default=False,
        ),
    ]