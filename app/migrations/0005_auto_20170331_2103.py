# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-31 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_vendorlisting_vendor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorlisting',
            name='vendor_bio',
            field=models.CharField(max_length=110),
        ),
    ]