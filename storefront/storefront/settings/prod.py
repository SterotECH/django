from .common import *
import dj_database_url
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    'sterobuy-prod.herokuapp.com',
    'django-production.up.railway.app',
    '0.0.0.0',
]


DATABASES = {
    'default': dj_database_url.config()
}

REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 2525
# DEFAULT_FROM_EMAIL = 'from@sterobuy.com'
