# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-06 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('faqs', wagtail.wagtailcore.fields.StreamField((('question_answer_block', wagtail.wagtailcore.blocks.StructBlock((('question', wagtail.wagtailcore.blocks.CharBlock(help_text='Введите часто задаваемый вопрос')), ('answer', wagtail.wagtailcore.blocks.TextBlock(help_text='Введите ответ'))))),), blank=True, verbose_name='Вопрос Ответ')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
