# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-02 10:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('simply_posted_accounts', '0005_auto_20170302_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentprovider',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2017, 3, 2, 10, 34, 31, 607238, tzinfo=utc), help_text='Enter the first name', max_length=50, verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contentprovider',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2017, 3, 2, 10, 34, 46, 278747, tzinfo=utc), help_text='Enter the last name', max_length=50, verbose_name='Last Name'),
            preserve_default=False,
        ),
    ]
