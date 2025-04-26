from django.conf.global_settings import STATICFILES_DIRS

from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'db_empleado',
        'USER':'django',
        'PASSWORD':'django',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
#STATICFILES_DIRS = [BASE_DIR.child('static')]
#STATICFILES_DIRS = BASE_DIR/'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]