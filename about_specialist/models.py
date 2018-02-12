from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from base.blocks import BaseContentBlock


class AboutSpecialistPage(Page):
    profession = models.CharField(
        "Специальность",
        max_length=250, blank=True,
    )
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        verbose_name="картинка",
    )
    main_info = models.TextField(
        blank=True,
        verbose_name="Основная краткая информация"
    )
    body = StreamField(
        BaseContentBlock,
        verbose_name='Основной текстовый блок',
        blank=True,
    )

    parent_page_types = ['home.HomePage']
    subpage_types = []

    content_panels = Page.content_panels + [
        ImageChooserPanel('photo'),
        FieldPanel('profession'),
        FieldPanel('main_info'),
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'О специалисте'
        verbose_name_plural = 'О специалисте'
