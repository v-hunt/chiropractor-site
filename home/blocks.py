from wagtail.wagtailcore.blocks import (
    StructBlock,
    URLBlock,
    CharBlock,
    StreamBlock,
    ChoiceBlock,
    TextBlock,
    ListBlock,
    PageChooserBlock,
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


class _IconChoiceBlock(ChoiceBlock):
    choices = (
        ('aids', 'aids'),
        ('ambulance', 'ambulance'),
        ('autism', 'autism'),
        ('bandage', 'bandage'),
        ('bed-patient', 'bed-patient'),
        ('blind', 'blind'),
        ('blood', 'blood'),
        ('blood-drop', 'blood-drop'),
        ('blood-test', 'blood-test'),
        ('capsule', 'capsule'),
        ('crutches', 'crutches'),
        ('dna', 'dna'),
        ('dna-alt-1', 'dna-alt-1'),
        ('doctor', 'doctor'),
        ('doctor-alt', 'doctor-alt'),
        ('drug', 'drug'),
        ('drug-pack', 'drug-pack'),
        ('eye-alt', 'eye-alt'),
        ('first-aid-alt', 'first-aid-alt'),
        ('garbage', 'garbage'),
        ('heart-alt', 'heart-alt'),
        ('heartbeat', 'heartbeat'),
        ('herbal', 'herbal'),
        ('hospital', 'hospital'),
        ('icu', 'icu'),
        ('injection-syringe', 'injection-syringe'),
        ('laboratory', 'laboratory'),
        ('medical-sign', 'medical-sign'),
        ('medical-sign-alt', 'medical-sign-alt'),
        ('nurse', 'nurse'),
        ('nurse-alt', 'nurse-alt'),
        ('nursing-home', 'nursing-home'),
        ('operation-theater', 'operation-theater'),
        ('paralysis-disability', 'paralysis-disability'),
        ('pills', 'pills'),
        ('prescription', 'prescription'),
        ('pulse', 'pulse'),
        ('stethoscope', 'stethoscope'),
        ('stethoscope-alt', 'stethoscope-alt'),
        ('stretcher', 'stretcher'),
        ('surgeon', 'surgeon'),
        ('surgeon-alt', 'surgeon-alt'),
        ('tablets', 'tablets'),
        ('test-bottle', 'test-bottle'),
        ('test-tube', 'test-tube'),
        ('thermometer-alt', 'thermometer-alt'),
        ('tooth', 'tooth'),
        ('xray', 'xray'),
    )

    class Meta:
        icon = 'cup'
        label = 'Иконка'
        help_text = "Иконки взяти с сайта http://icofont.com/icons/ " \
                    "с раздела Medical"


class _SingleDiseaseBlock(StructBlock):
    icon = _IconChoiceBlock()
    title = CharBlock(
        label='Название',
        max_length=19
    )


class DiseaseSectionBlock(StructBlock):
    headline = CharBlock(
        label='Заголовок секции',
    )
    text = TextBlock(
        label='Текст'
    )
    diseases = ListBlock(
        _SingleDiseaseBlock, label='Список заболеваний')

    class Meta:
        min_num = 1
        max_num = 1
        template = 'home/blocks/disease_section_block.html'


class _WhyChoseUsBlock(StructBlock):
    icon = _IconChoiceBlock()
    title = CharBlock(
        label='Название пункта',
        max_length=19
    )
    text = CharBlock(
        label='Текст под названием',
        max_length=80,
    )


class WhyChooseUsSectionBlock(StructBlock):
    headline = CharBlock(
        label='Заголовок секции',
    )
    text = TextBlock(
        label='Текст'
    )
    cards = ListBlock(
        _WhyChoseUsBlock, label='Список карточек', max_num=4)

    class Meta:
        min_num = 1
        max_num = 1
        template = 'home/blocks/why_choose_us_section_block.html'


class _MethodBlock(StructBlock):
    page = PageChooserBlock(
        'methods.MethodPage',
        label='Методика',
        help_text="Выберите методику для отображения на главной странице",
    )


class SelectedMethodsSection(StructBlock):
    headline = CharBlock(
        label='Заголовок секции',
    )
    text = TextBlock(
        label='Текст'
    )
    selected_methods = ListBlock(
        _MethodBlock,
        label='Методики',
        min_num=3,
        max_num=3,
    )

    class Meta:
        template = 'home/blocks/selected_methods_section_block.html'
