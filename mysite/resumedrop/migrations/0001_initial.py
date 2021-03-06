# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_year_text', models.CharField(default='Class Year', editable=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(default='Name', editable=False, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_text', models.CharField(default='Resume', editable=False, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Wpi_email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wpi_email_text', models.CharField(default='WPI Email', editable=False, max_length=9)),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='identifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumedrop.Wpi_email'),
        ),
        migrations.AddField(
            model_name='name',
            name='identifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumedrop.Wpi_email'),
        ),
        migrations.AddField(
            model_name='class_year',
            name='identifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumedrop.Wpi_email'),
        ),
    ]
