from .common import *
import dj_database_url
import os

DEBUG = True

SECRET_KEY = os.environ('SECRET_KEY')

ALLOWED_HOSTS = [
    'sterobuy-prod.herokuapp.com',
    'django-production.up.railway.app']


DATABASES = {
    'default': dj_database_url.config()
}
