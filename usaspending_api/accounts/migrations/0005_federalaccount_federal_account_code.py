# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-19 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170512_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='federalaccount',
            name='federal_account_code',
            field=models.TextField(null=True),
        ),
    ]
