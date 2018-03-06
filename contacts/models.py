from django.db import models
from django.core.validators import RegexValidator
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey

from .forms import ContactForm


class ContactPage(Page):
    body = RichTextField(
        "Текстовый блок",
    )
    address = models.CharField("Адрес", max_length=255)
    email = models.EmailField("E-mail")
    latitude = models.FloatField(
        "Широта",
        help_text="Используется в картах Google",
        default=50.451435
    )
    longitude = models.FloatField(
        "Долгота",
        help_text="Используется в картах Google",
        default=30.511989
    )
    facebook_link = models.URLField(
        "Facebook",
        help_text='Ссылка на страницу в Facebook',
        blank=True
    )
    instagram_link = models.URLField(
        "Instagram",
        help_text='Ссылка на страницу в Instagram',
        blank=True
    )

    parent_page_types = ['home.HomePage']
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('address'),
        FieldPanel('email'),
        InlinePanel('phones', label='Телефоны'),
        MultiFieldPanel(
            [FieldPanel('latitude'), FieldPanel('longitude')],
            heading="Координаты для карты Google"
        ),
        MultiFieldPanel(
            [FieldPanel('facebook_link'), FieldPanel('instagram_link')],
            heading="Социальные сервисы"
        )

    ]

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def get_context(self, request, *args, **kwargs):
        """
        Add ContactForm to the context.
        """
        context = super(ContactPage, self).get_context(request, *args, **kwargs)
        context['form'] = ContactForm()
        return context

    def main_phone(self):
        if self.phones.exists():
            return self.phones.first()


class PhoneNumber(Orderable):
    page = ParentalKey(ContactPage, related_name='phones')
    phone = models.CharField(
        "Телефон",
        max_length=15,
        validators=[
            RegexValidator(
                r"^\+\d+$",
                'Введите телефон в формате +888888888'
            ),
        ],
    )

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        """
        +380 088 888888
        """
        return self.phone[:4] + " " + self.phone[4:7] + " " + self.phone[7:]

    def to_str(self):
        return self.__str__()
