# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-02 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0006_merge_20170523_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltransactioncontract',
            name='ordering_period_end_date',
            field=models.TextField(blank=True, help_text='The end date for the ordering period', null=True),
        ),
        migrations.AlterField(
            model_name='transactioncontract',
            name='ordering_period_end_date',
            field=models.TextField(blank=True, help_text='The end date for the ordering period', null=True),
        ),
    ]
