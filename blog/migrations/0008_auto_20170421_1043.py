# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170420_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.ImageField(blank=True, null=True, upload_to='Post_list/%Y/%m/%d'),
        ),
    ]
