# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-16 01:41
from __future__ import unicode_literals

from django.db import migrations, models
from usaspending_api.references.models import AgencyByFain, AgencyByUri, AgencyByPiid, AgencyByToptier


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0005_auto_20170504_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyByFain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgac_code', models.TextField()),
                ('fain', models.TextField()),
            ],
            options={
                'db_table': 'agency_by_fain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AgencyByPiid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgac_code', models.TextField()),
                ('piid', models.TextField()),
                ('parent_award_id', models.IntegerField()),
            ],
            options={
                'db_table': 'agency_by_piid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AgencyByToptier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgac_code', models.TextField()),
            ],
            options={
                'db_table': 'agency_by_toptier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AgencyByUri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgac_code', models.TextField()),
                ('uri', models.TextField()),
            ],
            options={
                'db_table': 'agency_by_uri',
                'managed': False,
            },
        ),
        migrations.RunSQL(AgencyByFain.creation_sql, AgencyByFain.drop_sql),
        migrations.RunSQL(AgencyByUri.creation_sql, AgencyByUri.drop_sql),
        migrations.RunSQL(AgencyByPiid.creation_sql, AgencyByPiid.drop_sql),
        migrations.RunSQL(AgencyByToptier.creation_sql, AgencyByToptier.drop_sql),
    ]
