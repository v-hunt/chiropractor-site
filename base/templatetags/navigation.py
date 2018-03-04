import re
from django import template

from methods.models import MethodIndexPage, MethodPage
from about_specialist.models import AboutSpecialistPage
from faq.models import FaqPage
from pricing.models import PricingPage
from contacts.models import ContactPage


register = template.Library()


def _get_url_from_page_model(page_model):
    concrete_page = page_model.objects.live().first()
    return concrete_page.url if concrete_page else None


def _convert_model_name(name):
    """
    Convert CamelCase to snake_notation.

    See https://stackoverflow.com/a/1176023
    """
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@register.inclusion_tag('base/tags/main_menu.html')
def main_menu():
    models = [
        MethodIndexPage,
        AboutSpecialistPage,
        FaqPage,
        PricingPage,
        ContactPage
    ]
    urls = {
        _convert_model_name(model.__name__) + '_url': _get_url_from_page_model(model)
        for model in models
    }

    urls.update({
        'method_pages': MethodPage.objects.live(),
    })
    return urls
