from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class PricingPage(Page):
    body = RichTextField(
        verbose_name="Текст",
        help_text="Введите описание цен",
    )

    parent_page_types = ['home.HomePage']
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = "Стоимость"
        verbose_name_plural = "Стоимость"
