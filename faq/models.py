from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel

from .blocks import FaqBlock


class FaqPage(Page):
    faqs = StreamField(
        FaqBlock(), verbose_name="Вопрос Ответ", blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('faqs'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = 'страница FAQ'
        verbose_name_plural = 'страницы FAQ'

