# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-27 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simply_posted_calendar', '0002_auto_20170227_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='approved',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='publication',
            name='substituted_for',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simply_posted_calendar.Publication'),
        ),
    ]
