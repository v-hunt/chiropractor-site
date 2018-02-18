from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=250, min_length=3, required=True,
        label="Имя"
    )
    email = forms.EmailField(label='E-mail')
    subject = forms.CharField(
        max_length=150,
        label="Тема"
    )
    phone = forms.CharField(
        label="Телефон",
        required=False,
        min_length=10, max_length=15,
        widget=forms.TextInput(attrs={'type': 'tel'})
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Сообщение'
    )

    def send_mail(self):
        mail_message = """
        Сообщение от: {name}
        Телефон для связи: {phone_number}
        ===============================================================

        {message}
        """.format(
            name=self.cleaned_data['name'],
            phone_number=self.cleaned_data['phone'] or 'Не указан',
            message=self.cleaned_data['message'],
        )

        send_mail(
            subject='Сообщение с личного сайта: ' + self.cleaned_data['subject'],
            message=mail_message,
            from_email=self.cleaned_data['email'],
            recipient_list=settings.MAIL_TO,
            html_message=None
        )