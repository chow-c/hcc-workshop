# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-08 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_questions_image_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.CharField(choices=[('1', '1,2 - 1,2,6,3,5,4'), ('2', '1,2 - 2,3,1,4,6,5'), ('3', '1,2 - 3,4,2,5,1,6'), ('4', '1,2 - 4,5,3,6,2,1'), ('5', '1,2 - 5,6,4,1,3,2'), ('6', '1,2 - 6,1,5,2,4,3'), ('7', '2,1 - 1,2,6,3,5,4'), ('8', '2,1 - 2,3,1,4,6,5'), ('9', '2,1 - 3,4,2,5,1,6'), ('10', '2,1 - 4,5,3,6,2,1'), ('11', '2,1 - 5,6,4,1,3,2'), ('12', '2,1 - 6,1,5,2,4,3')], max_length=100)),
                ('tally', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='experimentpage',
            name='pid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]