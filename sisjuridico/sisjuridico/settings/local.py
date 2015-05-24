from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.postgresql_psycopg2',
        'NAME'     : 'bdex1',
        'USER'     : 'root',
        'PASSWORD' : '123',
        'HOST'     : 'localhost',
        'PORT'     : '5432',

    }
}

'''import pymysql
pymysql.install_as_MySQLdb() 

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'a',
        'USER'     : 'root',
        'PASSWORD' : '123',
        'HOST'     : 'localhost',
        'PORT'     : '3306',

    }
}'''

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
