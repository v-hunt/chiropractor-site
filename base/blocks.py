from wagtail.wagtailcore.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)


class BaseTextBlock(StructBlock):
    header = CharBlock(
        help_text="Введите заголовок текстового блока"
    )
    text = RichTextBlock(
        help_text="Введите текст блока",
        classname="full",
    )

    class Meta:
        icon = "title"
        template = "base/blocks/text_block.html"


class BaseContentBlock(StreamBlock):
    """
    Define content block (headers and body).
    """
    content = BaseTextBlock()
