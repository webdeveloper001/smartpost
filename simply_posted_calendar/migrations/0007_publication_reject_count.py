# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-07 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simply_posted_calendar', '0006_publication_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='reject_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
