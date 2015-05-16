from .base import *
import dj_database_url

ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME'  : 'd1q20vi89aouud',
        'USER'  : 'psdieurbhbvrrj',
        'PASSWORD' : 'XJivYvsdT9GTKHmM3uIewQBMFh',
        'HOST': '',
        'PORT': '',
    }
}

DATABASES['default'] =  dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static asset configuration

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)