# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='StringConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_string', models.CharField(help_text='Строка вверху страницы', max_length=70, verbose_name='строка вверху')),
                ('bottom_text', models.TextField(help_text='текст внизу страницы', max_length=200, verbose_name='текст внизу')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Текстовые константы',
            },
        ),
    ]