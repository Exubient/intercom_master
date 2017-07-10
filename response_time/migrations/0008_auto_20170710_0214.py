# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-10 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response_time', '0007_auto_20170710_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='usedConvo',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('author', models.TextField()),
                ('created_at', models.IntegerField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='admintable',
            name='averageResponse',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='admintable',
            name='convoCount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='admintable',
            name='firstResponse',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='admintable',
            name='medianResponse',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='admintable',
            name='realCount',
            field=models.FloatField(default=0),
        ),
    ]
