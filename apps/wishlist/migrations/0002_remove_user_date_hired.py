# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-24 23:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_hired',
        ),
    ]