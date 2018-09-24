# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0005_banda_costo_ensamblado'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='con_nombre_automatico',
            field=models.BooleanField(default=True, verbose_name='nombre automático'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='descripcion_comercial',
            field=models.CharField(default='AUTOMÁTICO', max_length=200),
        ),
        migrations.AlterField(
            model_name='banda',
            name='descripcion_estandar',
            field=models.CharField(default='AUTOMÁTICO', max_length=200),
        ),
        migrations.AlterField(
            model_name='ensamblado',
            name='cortado_a',
            field=models.CharField(default='COMPLETA', max_length=10, verbose_name='Cortado a'),
        ),
    ]