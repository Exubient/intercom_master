# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-10 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response_time', '0018_auto_20170710_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintable',
            name='array',
            field=models.TextField(default=None),
        ),
    ]
