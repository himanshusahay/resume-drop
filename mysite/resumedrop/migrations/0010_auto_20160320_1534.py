# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import resumedrop.models


class Migration(migrations.Migration):

    dependencies = [
        ('resumedrop', '0009_auto_20160320_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(blank=True, default='resumedrop/static/polls/resumes/default.txt', upload_to=resumedrop.models.content_file_name),
        ),
    ]