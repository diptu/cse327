# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_crop_fertilizer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizer',
            name='crop_name',
        ),
        migrations.AddField(
            model_name='crop',
            name='fertilizer_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.Fertilizer'),
            preserve_default=False,
        ),
    ]
