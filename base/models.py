from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailadmin.edit_handlers import FieldPanel


@register_setting
class StringConstants(BaseSetting):
    header_string = models.CharField(
        'строка вверху',
        help_text='Строка вверху страницы',
        max_length=70
    )
    bottom_text = models.TextField(
        'текст внизу',
        help_text='текст внизу страницы',
        max_length=200
    )

    panels = [
        FieldPanel('header_string'),
        FieldPanel('bottom_text'),
    ]

    class Meta:
        verbose_name = 'Текстовые константы'
