# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 20:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=20)),
                ('fecha_alta', models.DateTimeField(default=django.utils.timezone.now)),
                ('comprobante', models.ImageField(upload_to='comprobantes/%Y/%m/%d/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tipo', models.CharField(choices=[('Pago de Interes', 'Pago de interes'), ('Pago de cantidad invertida', 'Pago de cantidad invertida')], max_length=30)),
                ('fecha_alta', models.DateTimeField(default=django.utils.timezone.now)),
                ('comprobante', models.ImageField(upload_to='comprobantes/%Y/%m/%d/')),
                ('inversion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inversiones.Inversion')),
            ],
        ),
    ]
