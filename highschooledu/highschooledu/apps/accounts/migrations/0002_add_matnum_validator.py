# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 17:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='matnum',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Please enter a numeric value or leave the field blank.')]),
        ),
    ]
