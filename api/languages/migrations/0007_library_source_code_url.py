# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0006_auto_20151223_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='source_code_url',
            field=models.URLField(blank=True, default=b'', max_length=2048),
        ),
    ]