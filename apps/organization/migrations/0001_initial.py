# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-17 06:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u57ce\u5e02')),
                ('desc', models.CharField(max_length=200, verbose_name='\u57ce\u5e02\u63cf\u8ff0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u57ce\u5e02',
                'verbose_name_plural': '\u57ce\u5e02',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u673a\u6784\u540d\u79f0')),
                ('desc', models.TextField(verbose_name='\u673a\u6784\u63cf\u8ff0')),
                ('click_nums', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='\u5c01\u9762\u56fe')),
                ('address', models.CharField(max_length=150, verbose_name='\u673a\u6784\u5730\u5740')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='\u6240\u5728\u57ce\u5e02')),
            ],
            options={
                'verbose_name': '\u673a\u6784',
                'verbose_name_plural': '\u673a\u6784',
            },
        ),
    ]
