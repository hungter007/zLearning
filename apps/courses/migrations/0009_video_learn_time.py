# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-08-17 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='learn_time',
            field=models.IntegerField(default=0, verbose_name='学习时长（分钟）'),
        ),
    ]