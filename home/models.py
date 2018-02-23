from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from .blocks import (
    CarouselBlock,
    DiseaseSectionBlock,
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

    content_panels = Page.content_panels + [
        StreamFieldPanel('carousel'),
        StreamFieldPanel('diseases'),
    ]
