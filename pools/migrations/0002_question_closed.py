# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
