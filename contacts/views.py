from django.views.generic.edit import BaseFormView
from django.contrib import messages

from .forms import ContactForm


class ContactFormView(BaseFormView):
    http_method_names = ["post"]
    form_class = ContactForm
    success_url = '/contacts/'

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
