# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricingpage',
            options={'verbose_name': 'Стоимость', 'verbose_name_plural': 'Стоимость'},
        ),
    ]