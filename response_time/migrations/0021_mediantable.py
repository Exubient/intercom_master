# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-10 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('response_time', '0020_auto_20170710_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='medianTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responseTime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='response_time.AdminTable')),
            ],
        ),
    ]
