from .common import *

import os

DEBUG = True

SECRET_KEY = os.environ('SECRET_KEY')

ALLOWED_HOSTS = []


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
