# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_followup', '0007_auto_20181001_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]