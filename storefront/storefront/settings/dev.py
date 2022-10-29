from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-ce0j5uw8t!uw+0y)y1_sd_%qgu(9t%^#=2sb5g&*g8!y2lenhy'

INSTALLED_APPS += ['debug_toolbar', 'silk', ]

MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ALLOWED_HOSTS = [
    '0.0.0.0']


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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'USER': 'root',
        'PASSWORD': 'MyPassword',
        'HOST': 'mysql',
    },
}

CELERY_BROKER_URL = 'redis://redis:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/2',
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'from@sterobuy.com'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
