# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-09 10:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_auto_20170309_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouphost',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='hostlist',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
    ]
