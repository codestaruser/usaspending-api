# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-02 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0002_auto_20170503_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('term', models.TextField(db_index=True, unique=True)),
                ('data_act_term', models.TextField(blank=True, null=True)),
                ('plain', models.TextField(unique=True)),
                ('official', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DefinitionResource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('url', models.TextField()),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='references.Definition')),
            ],
            options={
                'managed': True,
                'db_table': 'definition_resource',
            },
        ),
    ]
