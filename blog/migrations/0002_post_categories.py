# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
