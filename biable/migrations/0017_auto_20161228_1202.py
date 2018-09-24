# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0016_vendedorbiable_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_terc_fa', models.CharField(max_length=20)),
                ('cliente', models.CharField(max_length=200)),
                ('tipo_documento', models.CharField(blank=True, max_length=3, null=True)),
                ('nro_documento', models.CharField(blank=True, max_length=10, null=True)),
                ('forma_pago', models.PositiveIntegerField(blank=True, null=True)),
                ('fecha_documento', models.DateField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('fecha_ultimo_pago', models.DateField(blank=True, null=True)),
                ('por_cobrar', models.DecimalField(decimal_places=4, max_digits=18)),
                ('retenciones', models.DecimalField(decimal_places=4, max_digits=18)),
                ('valor_contado', models.DecimalField(decimal_places=4, max_digits=18)),
                ('anticipo', models.DecimalField(decimal_places=4, max_digits=18)),
                ('a_recaudar', models.DecimalField(decimal_places=4, max_digits=18)),
                ('recaudado', models.DecimalField(decimal_places=4, max_digits=18)),
                ('debe', models.DecimalField(decimal_places=4, max_digits=18)),
                ('esta_vencido', models.BooleanField(default=False)),
                ('dias_vencido', models.PositiveIntegerField(blank=True, null=True)),
                ('dias_para_vencido', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='vendedorbiable',
            name='activo',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='cartera',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biable.VendedorBiable'),
        ),
    ]