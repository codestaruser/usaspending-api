# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-30 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0012_overalltotals'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrecMap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('agency_identifier', models.TextField(db_index=True)),
                ('main_account_code', models.TextField(db_index=True)),
                ('treasury_appropriation_account_title', models.TextField(db_index=True)),
                ('sub_function_code', models.TextField(db_index=True)),
                ('fr_entity_code', models.TextField()),
            ],
            options={
                'db_table': 'frec_map',
            },
        ),
    ]
