"""
Django settings for joinrpg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
import re
import configparser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-xg80#^t4gpteyw@226bqt2pdypyzxzq6sj+^*va#*@pi&rwvh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'claims.User'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'bootstrap3',
    'claims'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'joinrpg.urls'

WSGI_APPLICATION = 'joinrpg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

config = configparser.ConfigParser()
config.read("joinrpg.conf")

DATABASES = {
    'default': {
        'ENGINE': config.get('DATABASE', 'ENGINE', fallback='django.db.backends.sqlite3'),
        'HOST': config.get('DATABASE', 'HOST', fallback=''),
        'NAME': config.get('DATABASE', 'NAME', fallback='db.sqlite3'),
        'USER': config.get('DATABASE', 'USER', fallback=''),
        'PASSWORD': config.get('DATABASE', 'PASSWORD', fallback=''),
        'CHARSET': config.get('DATABASE', 'CHARSET', fallback='utf8')
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join (BASE_DIR, 'claims/templates/').replace('\\', '/'),
)