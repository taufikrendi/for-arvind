"""
Django settings for fintech-transactional project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config, Csv

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# TEMPLATE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
ENCRYPT_KEY = config('ENCRYPT_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # test data dump
    # 'autofixture',
    'account',
    'deposits',
    'loan',
    'transaction',
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

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'fintech-transactional/templates')],
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

WSGI_APPLICATION = 'wsgi.application'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher', #pbkdf2_sha256
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher', #pbkdf2_sha1
]

SALTED_PASSWORD = 'uH19IfSX6BEN2RH0dStAYExY/'
SALTED_PIN = '1NiIsInR5cCI6IkpXVCJ9./'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASE_ROUTERS = ['route.routers.TransactionRouter']

DATABASES = {
    'default': {
    },
    'default_slave': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'account_db',
        'USER': 'account_master_db',
        'PASSWORD': 'secret_password',
        'HOST': 'bitnami-docker-postgresql_postgresql-account-slave_1',
        'PORT': '5432',
    },
    'funds_slave': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'funds_db',
        'USER': 'funds_master_db',
        'PASSWORD': 'secret_password',
        'HOST': 'bitnami-docker-postgresql_postgresql-funds-slave_1',
        'PORT': '5432',
    },
    'transaction_master': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'transaction_db',
        'USER': 'transaction_master_db',
        'PASSWORD': 'secret_password',
        'HOST': 'bitnami-docker-postgresql_postgresql-transaction-master_1',
        'PORT': '5432',
    },
    'transaction_slave': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'transaction_db',
        'USER': 'transaction_master_db',
        'PASSWORD': 'secret_password',
        'HOST': 'bitnami-docker-postgresql_postgresql-transaction-slave_1',
        'PORT': '5432',
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
        'OPTIONS': {
                    'min_length': 8,
                }
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

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/var/log/django.log",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True
        },
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = (os.path.join(BASE_DIR))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATICFILES_DIRS = [
    os.path.join(STATIC_ROOT, "fintech-transactional/static"),
]

STATICFILES_FINDER = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

INTERNAL_IPS = [
    '127.0.0.1',
]
# AUTH_USER_MODEL = 'auth.User'
# LOGIN_REDIRECT_URL = 'home/'
APPEND_SLASH = True
DOMAIN_CONFIGURATION = '127.0.0.1:5000'
PASSWORD_RESET_TIMEOUT_DAYS = 1
###################################
# Captcha - google.com/recaptcha
###################################
RECAPTCHA_SECRET_KEY = '6LfFllcUAAAAAAjeZYBYG9h6TWsO__7Rh5ABKAnz'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# MAILER_EMAIL_BACKEND = EMAIL_BACKEND
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'taufik.rendi.anggara@gmail.com'
# EMAIL_HOST_PASSWORD = 'helldark@19'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SILKY_PYTHON_PROFILER = True
# SILKY_PYTHON_PROFILER_BINARY = True
SILKY_ANALYZE_QUERIES = True
SILKY_AUTHENTICATION = True
SILKY_AUTHORISATION = True

#SESSION CONFIGURATION
# SESSION_COOKIE_NAME = 'fin_cookie'
# SESSION_CACHE_ALIAS = 'fin_session'
SESSION_COOKIE_AGE = 1209600
# SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#CSRF CONFIGURATION
# CSRF_COOKIE_SECURE = True

#KAFKA
KAFKA_SERVER = 'dokaf_kafka_1:9092'
# KAFKA_MECHANISM = 'PLAIN'
# KAFKA_SECURITY = 'SASL_SSL'
# KAFKA_USERNAME = 'avnadmin'
# KAFKA_PASSWORD = 'hb6vk634bbnz39ab'

#KAFKA SCHEMES
# SCHEMA_REGISTRY_URL = 'http://localhost:8081'
# SCHEMA_KEY = 'VENATWOLOELN3LWG'
# SCHEMA_SECRET = 'KDohaIOlmikTW+s7CS1ZK4PBS9+Rs6eUKW42/0BBjGKhCQoQMDnhsoO6fMr5ZZeE'
# AUTH_INFO = 'avnadmin'
# AUTH_CREDENTIALS = 'hb6vk634bbnz39ab'

#FASTAPI
KEY_HASHED = "76512137f867a346e540e67235ea1dcf4dde21e4e9fc6fc452b1080845795fc7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30