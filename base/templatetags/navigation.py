import re
from django import template
from typing import List

from methods.models import MethodIndexPage, MethodPage
from about_specialist.models import AboutSpecialistPage
from faq.models import FaqPage
from pricing.models import PricingPage
from contacts.models import ContactPage


register = template.Library()


PAGES = (
    ("Методики", MethodIndexPage),
    ("О специалисте", AboutSpecialistPage),
    ("FAQ", FaqPage),
    ("Стоимость", PricingPage),
    ("Контакты", ContactPage),
)


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


def _get_urls_for_models(models: List) -> dict:
    return {
        _convert_model_name(model.__name__) + '_url': _get_url_from_page_model(model)
        for model in models
    }


@register.inclusion_tag('base/tags/main_menu.html')
def main_menu():
    models = [
        MethodIndexPage,
        AboutSpecialistPage,
        FaqPage,
        PricingPage,
        ContactPage
    ]
    urls = _get_urls_for_models(models)

    urls.update({
        'method_pages': MethodPage.objects.live(),
    })
    return urls


@register.inclusion_tag('base/tags/footer_links.html')
def footer_links():
    urls = [{'title': title, 'url': _get_url_from_page_model(page)} for title, page in PAGES]
    return {'urls': urls}


@register.inclusion_tag('base/tags/footer_social_serv_links.html')
def footer_social_serv_links():
    contact_page = ContactPage.objects.live().first()

    if contact_page:
        return {
            'facebook_link': contact_page.facebook_link,
            'instagram_link': contact_page.instagram_link,
        }

    else:
        return {
            'facebook_link': None,
            'instagram_link': None,
        }
