# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-09 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(default='', max_length=30, verbose_name='\u533f\u540d')),
                ('birday', models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('gender', models.CharField(choices=[('maile', '\u7537'), ('female', '\u5973')], default='female', max_length=10)),
                ('address', models.CharField(default='', max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
    ]
