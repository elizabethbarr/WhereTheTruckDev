# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-10-10 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_privacypolicy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrivacyPolicy',
        ),
    ]