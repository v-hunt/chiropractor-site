from wagtail.wagtailcore.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)


class QuestionAnswerBlock(StructBlock):
    question = CharBlock(
        help_text="Введите часто задаваемый вопрос"
    )
    answer = TextBlock(
        help_text="Введите ответ"
    )

    class Meta:
        icon = "title"
        template = "faq/blocks/question_answer_block.html"


class FaqBlock(StreamBlock):
    """
    Define the custom blocks for FAQs.
    """
    question_answer_block = QuestionAnswerBlock()
