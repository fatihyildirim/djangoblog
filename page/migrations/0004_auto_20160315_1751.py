# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_page_b_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='b_image',
            field=models.ImageField(blank=True, null=True, upload_to='page_background', verbose_name='Header Image'),
        ),
    ]
