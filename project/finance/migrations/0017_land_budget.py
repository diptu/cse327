# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0016_auto_20171126_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='budget',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.Budget'),
            preserve_default=False,
        ),
    ]
