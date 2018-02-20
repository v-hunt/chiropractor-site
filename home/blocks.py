from wagtail.wagtailcore.blocks import (
    StructBlock,
    URLBlock,
    CharBlock,
    StreamBlock,
)
from wagtail.wagtailimages.blocks import ImageChooserBlock


class _CarouselElementBlock(StructBlock):
    image = ImageChooserBlock(
        label='Картинка',
        help_text="Картинка для карусели (минимум 1920х900)"
    )
    headline = CharBlock(
        max_length=50,
        help_text="Заголовок картинки карусели",
        label='Заголовок',
    )
    caption = CharBlock(
        max_length=50,
        help_text="Подпись к заголовку",
        label='Подпись',
    )
    link = URLBlock(
        required=False,
        help_text="Ссылка (опционально)",
        label='Ссылка',
    )

    class Meta:
        icon = 'cogs'
        label = 'Элемент карусели'


class CarouselBlock(StreamBlock):
    carousel_element = _CarouselElementBlock()

    class Meta:
        min_num = 2
        max_num = 4
        template = 'home/blocks/carousel_block.html'
