# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0012_auto_20171125_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenue',
            name='budget',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.Budget'),
            preserve_default=False,
        ),
    ]