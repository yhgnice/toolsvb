# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-09 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='grouphost',
            fields=[
                ('f_group_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u5e73\u53f0ID')),
                ('f_group_name', models.CharField(max_length=20, verbose_name='\u5e73\u53f0\u540d\u79f0')),
                ('group_context', models.TextField(default='', max_length=20, null=True, verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u7ec4',
                'verbose_name_plural': '\u670d\u52a1\u5668\u7ec4',
            },
        ),
        migrations.AddField(
            model_name='hostlist',
            name='f_groups_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='hosts.grouphost', verbose_name='\u5e73\u53f0ID'),
            preserve_default=False,
        ),
    ]
