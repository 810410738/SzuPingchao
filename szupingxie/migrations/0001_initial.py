# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-16 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZhaoXinBaoMing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=2)),
                ('college', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('stu_no', models.CharField(max_length=20)),
            ],
        ),
    ]