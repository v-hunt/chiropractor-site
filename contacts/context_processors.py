from .models import ContactPage


def contacts(request):
    if ContactPage.objects.live().exists():
        return {
            'contacts': ContactPage.objects.live().first()
        }
