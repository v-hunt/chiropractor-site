from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from .blocks import (
    CarouselBlock,
    DiseaseSectionBlock,
    WhyChooseUsSectionBlock,
)


class HomePage(Page):
    carousel = StreamField(
        CarouselBlock(),
        blank=True,
    )

    diseases = StreamField([
        ('болезни', DiseaseSectionBlock()),
    ],
        blank=True,
        verbose_name='Список заболеваний',
    )

    why_choose_us = StreamField([
        ('why_choose_us', WhyChooseUsSectionBlock()),
    ],
        blank=True,
        verbose_name='Почему выбрать нас',
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('carousel'),
        StreamFieldPanel('diseases'),
        StreamFieldPanel('why_choose_us'),
    ]
