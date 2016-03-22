"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import environ

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3)a(u-im-v28w&o4m85yr1l*&%e-lkebwkxblk@$cs@#&j$d#9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Don't allow client side JavaScript
# CSRF_COOKIE_HTTPONLY = True
# SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
# Application definition

INSTALLED_APPS = [
    'resumedrop.apps.ResumedropConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django_s3_storage',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# for dj-database-url
# db_url = os.path.join(BASE_DIR, 'db.sqlite3')
# DATABASE['default'] = dj_database_url.parse('sqlite:////'+db_url, conn_max_age=600)

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

DATABASES = {'default': env.db_url()}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# S3 stuff

DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
AWS_S3_BUCKET_NAME = env.str('AWS_S3_BUCKET_NAME')
AWS_S3_BUCKET_NAME_STATIC = env.str('AWS_S3_BUCKET_NAME_STATIC')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
AWS_REGION = env.str('AWS_REGION')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'resumedrop/static/polls'),
)
