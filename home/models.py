from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from .blocks import CarouselBlock


class HomePage(Page):
    carousel = StreamField(
        CarouselBlock(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('carousel'),
    ]
