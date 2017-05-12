# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0005_auto_20170504_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalentity',
            name='category_8a_program_participant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_ability_one_program',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_alaskan_native_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_american_indian_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_asian_pacific_american_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_authorities_and_commissions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_black_american_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_community_developed_corporation_owned_firm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_community_development_corporations',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_dot_certified_disadvantaged_business_enterprise',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_economically_disadvantaged_women_owned_small_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_emerging_small_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_federally_funded_research_and_development_corp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_foreign_government',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_foreign_owned_and_located_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_foreign_owned_and_us_located_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_foundation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_government',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_higher_education',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_hispanic_american_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_historically_underutilized_business_firm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_indian_native_american_tribal_government',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_individuals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_international_organization',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_joint_venture_economically_disadvantaged_women_owned_small_business',
            field=models.BooleanField(db_column='category_jvwosb', default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_joint_venture_women_owned_small_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_labor_surplus_area_firm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_local_government',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_minority_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_minority_serving_institution_of_higher_education',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_national_government',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_native_american_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_native_hawaiian_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_nonprofit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_other_minority_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_other_than_small_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_private_institution_of_higher_education',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_public_institution_of_higher_education',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_regional_and_state_government',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_sba_certified_8a_joint_venture',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_self_certified_small_disadvanted_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_service_disabled_veteran_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_small_agricultural_cooperative',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_small_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_small_disadvantaged_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_special_designations',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_subcontinent_asian_indian_american_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_tribally_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_us_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_us_territory_or_possession',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_veteran_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_woman_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_women_owned_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='category_women_owned_small_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='contracting_officers_determination_of_business_size',
            field=models.TextField(blank=True, null=True),
        ),
    ]
