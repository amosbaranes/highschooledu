from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'highschooledu',
        'USER': 'highschooledu',
        'PASSWORD': 'highschooledu',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

CURRENT_URL = 'dev'