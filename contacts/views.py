from django.views.generic.edit import BaseFormView
from django.contrib import messages

from .forms import ContactForm
from .models import ContactPage


class ContactFormView(BaseFormView):
    http_method_names = ["post"]
    form_class = ContactForm

    def get_success_url(self):
        contact_page = ContactPage.objects.live().first()
        return contact_page.url

    def handle_form_valid(self, request, form):
        form.send_mail()
        messages.add_message(
            request, messages.SUCCESS,
            "Ваше сообщение отправлено! Мы свяжемся с Вами в ближайшее время."
            )
        return super(ContactFormView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.handle_form_valid(request, form)
        else:
            return self.form_invalid(form)
