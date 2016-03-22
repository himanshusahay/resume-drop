# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumedrop', '0012_auto_20160321_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(upload_to='resumes/'),
        ),
    ]