# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumedrop', '0002_major'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='class_year',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='major',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='name',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='identifier',
        ),
        migrations.DeleteModel(
            name='Class_year',
        ),
        migrations.DeleteModel(
            name='Major',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='Wpi_email',
        ),
    ]
