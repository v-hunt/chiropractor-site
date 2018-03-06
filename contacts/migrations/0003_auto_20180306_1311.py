# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20180213_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='facebook_link',
            field=models.URLField(blank=True, help_text='Ссылка на страницу в Facebook', verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='instagram_link',
            field=models.URLField(blank=True, help_text='Ссылка на страницу в Instagram', verbose_name='Instagram'),
        ),
    ]