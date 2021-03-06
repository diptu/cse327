# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_auto_20171125_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_fee', models.DecimalField(decimal_places=2, max_digits=20)),
                ('irrigation_fee', models.DecimalField(decimal_places=2, max_digits=20)),
                ('other_cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('crop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='finance.Crop')),
                ('land', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='finance.Land')),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='finance.Budget')),
            ],
        ),
    ]
