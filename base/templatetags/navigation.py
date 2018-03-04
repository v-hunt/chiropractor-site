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


@register.inclusion_tag('base/tags/main_menu.html')
def main_menu():
    return {
        'method_index_page_url': _get_url_from_page_model(MethodIndexPage),
        'method_pages': MethodPage.objects.live(),
        'about_specialist_page_url': _get_url_from_page_model(AboutSpecialistPage),
        'faq_page_url': _get_url_from_page_model(FaqPage),
        'pricing_page_url': _get_url_from_page_model(PricingPage),
        'contact_page_url': _get_url_from_page_model(ContactPage),
    }
