# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20170611_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/post/%Y%m'),
        ),
    ]
