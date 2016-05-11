# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='poids',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='prix',
            field=models.FloatField(blank=True, null=True),
        ),
    ]