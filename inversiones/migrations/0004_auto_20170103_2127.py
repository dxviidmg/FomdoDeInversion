# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inversiones', '0003_auto_20170103_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='comprobante',
            field=models.ImageField(upload_to='Pago/comprobantes/%Y/%m/%d/'),
        ),
    ]
