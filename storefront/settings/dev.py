from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-ce0j5uw8t!uw+0y)y1_sd_%qgu(9t%^#=2sb5g&*g8!y2lenhy'

MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1'
    # ...
]


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'storefront',
    #     'HOST': 'localhost',
    #     'USER': 'stero',
    #     'PASSWORD': 'code .',
    # },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'storefront',
        'USER': 'stero',
        'PASSWORD': 'code .',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
