# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0019_auto_20171207_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='total_share',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]
