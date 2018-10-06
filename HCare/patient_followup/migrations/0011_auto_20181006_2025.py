# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-06 18:25
from __future__ import unicode_literals

import datetime
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import patient_followup.models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_followup', '0010_auto_20181003_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('content', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/media//documents/', location='C:\\projets\\web_development\\django\\HCare\\HCare\\media/documents/'), upload_to=patient_followup.models.document_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 10, 6, 20, 25, 14, 358814))),
                ('diagnostic', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='appointement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 6, 20, 25, 14, 357815)),
        ),
        migrations.AlterField(
            model_name='appointement',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appointements', to='patient_followup.Patient'),
        ),
        migrations.AddField(
            model_name='medicalexam',
            name='appointement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_followup.Appointement'),
        ),
        migrations.AddField(
            model_name='document',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='patient_followup.MedicalExam'),
        ),
    ]
