# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_sessions', '0002_auto_20170705_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cohort',
            options={'ordering': ['starting_date']},
        ),
    ]