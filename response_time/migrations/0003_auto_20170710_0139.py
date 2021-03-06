# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-10 01:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('response_time', '0002_longconvo_part'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminHour',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='array',
            new_name='adminId',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='name',
            new_name='adminName',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='average_count',
            new_name='averageReponse',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='average_time',
            new_name='convoCount',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='averate_rt',
            new_name='firstReponse',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='convo_count',
            new_name='medianResponse',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='first_count',
            new_name='realCount',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='first_rt',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='first_time',
        ),
    ]
