# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0026_user_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.IntegerField(default=0),
        ),
    ]
