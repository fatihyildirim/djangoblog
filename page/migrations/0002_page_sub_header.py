# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='sub_header',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
