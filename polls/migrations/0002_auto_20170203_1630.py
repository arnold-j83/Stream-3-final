# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vode',
            new_name='Vote',
        ),
    ]
