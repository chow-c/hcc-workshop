# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20160930_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshopuser',
            name='level',
            field=models.CharField(choices=[('0', '0 - Baby'), ('1', '1 - Student'), ('2', '2 - Teacher'), ('3', '3 - Doctor'), ('4', '4 - Professor'), ('5', '5 - Mad Scientist'), ('6', '6 - Superhero'), ('7', '7 - Alien'), ('8', '8 - Wizard'), ('9', '9 - A.I.')], default='0', max_length=100),
        ),
    ]
