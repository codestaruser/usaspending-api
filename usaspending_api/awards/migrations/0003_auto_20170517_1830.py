# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-17 18:30
from __future__ import unicode_literals

from django.db import migrations
from usaspending_api.etl.award_helpers import update_award_categories


def forwards_func(apps, schema_editor):
    update_award_categories()


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_award_category'),
    ]

    operations = [
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
    ]
