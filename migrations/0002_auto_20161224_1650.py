# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 13:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('Django_Example', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
