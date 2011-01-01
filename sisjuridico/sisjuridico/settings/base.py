from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'ni$cqsj*j5ld(r4b2k*hs&d#6$6!7(7i@=^bvkoivtbw%0^etn'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    )

THIRD_PARTY_APPS = (
    'axes',
    )

LOCAL_APPS = (
    'apps.busqueda',
    'apps.expediente',
    'apps.matenimiento',
    'apps.reportes',
    'apps.seguridad',
    )

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'axes.middleware.FailedLoginMiddleware',
)

ROOT_URLCONF = 'sisjuridico.urls'

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
MEDIA_ROOT = BASE_DIR.child('media')

WSGI_APPLICATION = 'sisjuridico.wsgi.application'
AUTH_USER_MODEL = 'seguridad.User'

#configuración de accesos
AXES_LOGIN_FAILURE_LIMIT = 5


#AXES_LOCKOUT_URL = "/opt/sisJuridico2/sisjuridico/templates/"
#AXES_LOCKOUT_TEMPLATE = 'seguridad/useBlock/block.html'
#print (AXES_LOCKOUT_TEMPLATE)