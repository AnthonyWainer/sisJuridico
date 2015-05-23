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
    'authtools',
    'django_admin_bootstrapped',
    'crispy_forms',
    'easy_thumbnails',
    'profiles',
    )

LOCAL_APPS = (
    'apps.cuentas',
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


WSGI_APPLICATION = 'sisjuridico.wsgi.application'

from django.core.urlresolvers import reverse_lazy
# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("apps.seguridad:index")
LOGIN_URL = reverse_lazy("apps.cuentas:login")
CRISPY_TEMPLATE_PACK = 'bootstrap3'