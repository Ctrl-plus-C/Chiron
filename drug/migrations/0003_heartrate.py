# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-26 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0002_auto_20190126_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpm', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]