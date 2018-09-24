# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-04 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('biable', '0026_cartera_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineavendedorbiable',
            name='colaborador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mi_vendedor_biable', to='usuarios.UserExtended'),
        ),
        migrations.AlterField(
            model_name='cartera',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mis_carteras', to='biable.VendedorBiable'),
        ),
    ]