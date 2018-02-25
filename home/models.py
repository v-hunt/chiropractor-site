from __future__ import absolute_import, unicode_literals

from django.db import models
from django.apps import apps

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from .blocks import (
    CarouselBlock,
    DiseaseSectionBlock,
    WhyChooseUsSectionBlock,
    SelectedMethodsSection,
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

    selected_methods = StreamField([
        ('selected_methods', SelectedMethodsSection())
    ],
        blank=True,
        verbose_name='Выбраные методики'
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('carousel'),
        StreamFieldPanel('diseases'),
        StreamFieldPanel('why_choose_us'),
        StreamFieldPanel('selected_methods'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)

        MethodIndexPage = apps.get_model('methods.MethodIndexPage')
        exist = MethodIndexPage.objects.exists()

        if exist:
            context['methods_index_page'] = MethodIndexPage.objects.first()
        else:
            context['methods_index_page'] = None

        return context
