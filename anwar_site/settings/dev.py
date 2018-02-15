from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0u^35+s3lvrrao4oqq-ci)k+cvv$r4!z+g4^4pk#8-lmc6ll6t'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MAIL_TO = [
    'anwar@example.com',
    ]


try:
    from .local import *
except ImportError:
    pass
