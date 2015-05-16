from .base import *
import dj_database_url

ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME'  : 'd2c0out1l093pk',
        'USER'  : 'ieljqjlbokceos',
        'PASSWORD' : 'laY6dqy3j0lbX8FBoP9z2cwUam',
        'HOST': '',
        'PORT': '',
    }
}

DATABASES['default'] =  dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static asset configuration

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_ROOT = 'media'

STATICFILES_DIRS = [BASE_DIR.child('static')]
