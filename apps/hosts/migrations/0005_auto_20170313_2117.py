# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-13 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0004_auto_20170313_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostlist',
            name='f_host_user',
            field=models.CharField(default='root', max_length=20, verbose_name='\u7528\u6237'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='f_groups_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosts.GroupHost', verbose_name='\u5e73\u53f0ID'),
        ),
    ]
