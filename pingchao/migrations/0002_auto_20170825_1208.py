# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-25 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingchao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teengame1',
            name='id_card',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teengame1',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
