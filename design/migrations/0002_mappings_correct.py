# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappings',
            name='correct',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]