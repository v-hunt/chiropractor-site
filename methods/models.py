from django.db import models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, StreamFieldPanel
    )


class MethodIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['methods.MethodPage']

    class Meta:
        verbose_name = 'Методики (список)'
        verbose_name_plural = 'Методики (список)'


class MethodPage(Page):
    overview = models.TextField("Краткое описание", max_length=250)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        verbose_name="картинка",
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('overview', classname="full"),
    ]
    parent_page_types = ['methods.MethodIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = 'Методика'
        verbose_name_plural = 'Методика'
