"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from environs import Env

from garpix_user.settings import *  # noqa

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

SITE_URL = os.getenv('SITE_URL')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'public', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'public', 'media')

TEMPLATES_PATH = os.path.join(BASE_DIR, '..', 'frontend', 'templates')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'frontend', 'static'),
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'eqator',
    'ckeditor',
    'celery',
    # for auth
    'rest_framework',
    'rest_framework.authtoken',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    # 'drf_multiple_model',
    'drf_spectacular',
    'garpix_package',
    # for notify
    'fcm_django',
    'garpix_notify',
    'garpix_user',
    'solo',
    'app',
    'user'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_PATH
        ],
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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env.int('POSTGRES_PORT'),
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# garpix_user

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'garpix_user.rest.authentication.MainAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

AUTHENTICATION_BACKENDS = (
    # Only your social networks
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    # Django
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'garpix_user.utils.backends.CustomAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details'
)

# GARPIX_ACCESS_TOKEN_TTL_SECONDS = 86400  # 24 hours
GARPIX_ACCESS_TOKEN_TTL_SECONDS = 0  # infinity
# GARPIX_ACCESS_TOKEN_TTL_SECONDS = 86400 * 14  # 14 days
GARPIX_REFRESH_TOKEN_TTL_SECONDS = 0  # infinity

MIGRATION_MODULES = {
    'garpix_user': 'app.migrations.garpix_user',
    'garpix_notify': 'app.migrations.garpix_notify',
}

AUTH_USER_MODEL = 'user.User'

# ckeditor

CKEDITOR_UPLOAD_PATH = ''

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': '100%',
    },
}

API_URL = 'api'

# user settings
GARPIX_USER = {
    # base settings
    'USE_REFERRAL_LINKS': False,
    'REFERRAL_REDIRECT_URL': '/',
    # email/phone confirmation
    'USE_EMAIL_CONFIRMATION': True,
    'USE_PHONE_CONFIRMATION': True,
    'USE_PREREGISTRATION_EMAIL_CONFIRMATION': True,
    'USE_PREREGISTRATION_PHONE_CONFIRMATION': True,
    'USE_EMAIL_LINK_CONFIRMATION': False,
    'CONFIRM_PHONE_CODE_LENGTH': 6,
    'CONFIRM_EMAIL_CODE_LENGTH': 6,
    'TIME_LAST_REQUEST': 1,
    'CONFIRM_PHONE_CODE_LIFE_TIME': 5,  # in minutes
    'CONFIRM_EMAIL_CODE_LIFE_TIME': 2,  # in days
    'CONFIRMATION_DELAY': 10,  # in days
    # restore password
    'USE_RESTORE_PASSWORD': True,
    # registration
    'USE_REGISTRATION': False,
    'REGISTRATION_SERIALIZER': 'app.serializers.RegistrationCustSerializer',
    'ADMIN_PASSWORD_SETTINGS': True,
    'MIN_LENGTH_PASSWORD': 8,
    'MIN_DIGITS_PASSWORD': 2,
    'MIN_CHARS_PASSWORD': 2,
    'MIN_UPPERCASE_PASSWORD': 1,
    'MIN_SPECIAL_PASSWORD': 1,
    'PASSWORD_HISTORY': 1,
    'PASSWORD_VALIDITY_PERIOD': -1,
    'PASSWORD_FIRST_CHANGE': False,
    'PASSWORD_VALIDITY_INFORM_DAYS': -1,
    # log in
    'AVAILABLE_ATTEMPT': -1,
    'ACCESS_TOKEN_TTL_SECONDS': 0,
    'REFRESH_TOKEN_TTL_SECONDS': 0
}

GARPIX_NOTIFY_CELERY_SETTINGS = 'app.celery.app'

NOTIFY_EVENTS = {}

NOTIFY_EVENTS.update(GARPIX_USER_NOTIFY_EVENTS)  # noqa

CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]

GARPIXCMS_CELERY_SETTINGS = 'app.celery.app'

ISO_LOGS_NAME = "garpix_user"
ISO_LOGS_PRODUCT = "Garpix user"
IB_ISO_LOGS_NAME = 'garpix_user_ib'
SYSTEM_ISO_LOGS_NAME = 'garpix_user_system'
INTERVAL_COUNT = 1
BACKUP_COUNT = 0
WHEN = 'D'


class GenerateFilesLogsData:
    """ Генератор файлов для сельдерея """

    def __init__(self, file_name):
        self.file_name = file_name

    def __generate_logs_file(self):
        directory = f'logs/{self.file_name}'
        if not os.path.isdir(directory):
            os.makedirs(directory)
        return f'{directory}/{self.file_name}.log'

    @classmethod
    def execute(cls, file_name):
        return cls(file_name).__generate_logs_file()


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)-4s %(name)-12s %(levelname)-12s %(message)s'
        },
        'file': {
            'format': '%(asctime)-4s %(name)-12s %(levelname)-12s %(message)s'
        },
        'file_iso': {
            '()': 'django.utils.log.ServerFormatter',
            'format': f'%(message)s'
        }
    },
    'handlers': {
        ISO_LOGS_NAME: {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'backupCount': BACKUP_COUNT,
            'formatter': 'file_iso',
            'interval': INTERVAL_COUNT,
            'when': WHEN,
            'filename': GenerateFilesLogsData.execute(ISO_LOGS_NAME),
        },
        IB_ISO_LOGS_NAME: {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'backupCount': BACKUP_COUNT,
            'formatter': 'file_iso',
            'interval': INTERVAL_COUNT,
            'when': WHEN,
            'filename': GenerateFilesLogsData.execute(IB_ISO_LOGS_NAME),
        },
        SYSTEM_ISO_LOGS_NAME: {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'backupCount': BACKUP_COUNT,
            'formatter': 'file_iso',
            'interval': INTERVAL_COUNT,
            'when': WHEN,
            'filename': GenerateFilesLogsData.execute(SYSTEM_ISO_LOGS_NAME),
        }
    },
    'loggers': {
        ISO_LOGS_NAME: {
            'handlers': [ISO_LOGS_NAME],
            'level': 'INFO',
            'propagate': False
        },
        IB_ISO_LOGS_NAME: {
            'handlers': [IB_ISO_LOGS_NAME],
            'level': 'INFO',
            'propagate': False
        },
        SYSTEM_ISO_LOGS_NAME: {
            'handlers': [SYSTEM_ISO_LOGS_NAME],
            'level': 'INFO',
            'propagate': False
        }
    }
}
