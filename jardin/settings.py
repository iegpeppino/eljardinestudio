"""
Django settings for jardin project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import json
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zekjy+$w(2mmh1(ygc4=60-_ptuf*2zhu!+=795855ctoa6mp8'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['localhost','127.0.0.1','eljardinestudio.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jardinpage.apps.JardinpageConfig',
    'django_cleanup.apps.CleanupConfig',
    'storages',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jardin.urls'

DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ './jardin/templates'],
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

WSGI_APPLICATION = 'jardin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dd0uu61c66sss9',
        'PASSWORD': os.getenv('JARDIN_PASS'),
        'HOST': 'ec2-18-208-24-104.compute-1.amazonaws.com',
        'PORT': '5432',
        'USER': 'ulslqdvxgdcygl',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_URL = '/static/'

#GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
# Google bucket credentials

# from lib.google.cloud import storage

# from lib.google.oauth2 import service_account

# # the json credentials stored as env variable
# json_str = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
# # project name
# gcp_project = os.environ.get('GCP_PROJECT') 

# # generate json - if there are errors here remove newlines in .env
# json_data = json.loads(json_str)
# # the private_key needs to replace \n parsed as string literal with escaped newlines
# json_data['private_key'] = json_data['private_key'].replace('\\n', '\n')

# # use service_account to generate credentials object
# credentials = service_account.Credentials.from_service_account_info(
#     json_data)

# # pass credentials AND project name to new client object (did not work wihout project name)
# storage_client = storage.Client(
#     project=gcp_project, credentials=credentials)


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('JARDIN_ACCESS_KEY')

AWS_SECRET_ACCESS_KEY = os.environ.get('JARDIN_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = 'eljardinestudio'

AWS_S3_CUSTOM_DOMAIN = f'eljardinestudio.s3.amazonaws.com'

AWS_QUERYSTRING_AUTH = False

MEDIA_URL = '/images/'

MEDIA_ROOT =  BASE_DIR / 'static/images'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if os.getcwd() == '/app':
    DEBUG = False