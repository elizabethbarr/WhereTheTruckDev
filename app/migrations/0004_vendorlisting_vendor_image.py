# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-31 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_vendorlisting_vendor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorlisting',
            name='vendor_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
