# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-13 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumedrop', '0004_auto_20160311_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='resume',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
