# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_followup', '0006_auto_20180927_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
