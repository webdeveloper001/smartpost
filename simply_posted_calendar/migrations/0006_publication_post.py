# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-06 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simply_posted_accounts', '0010_socialprofile'),
        ('simply_posted_calendar', '0005_auto_20170227_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='simply_posted_accounts.Post'),
            preserve_default=False,
        ),
    ]
