from django.conf import settings


def global_settings(request):
    return {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
}
