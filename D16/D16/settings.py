"""
Django settings for D16 project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)b_qc12l#u3(=e^o*vtxzbxqw4t#)jig#=6p@jv=is&r8zzd1('

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_apscheduler',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'APPS.bulletin_board',
    'ckeditor',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',  # FOR CACHES
    'django.middleware.common.CommonMiddleware',  # FOR CACHES
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',  # FOR CACHES
]

ROOT_URLCONF = 'D16.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'TEMPLATES')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

########################################################################################################################

# FOR ALLAUTH

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

########################################################################################################################

WSGI_APPLICATION = 'D16.wsgi.application'

########################################################################################################################

# DATABASE SETTINGS

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

########################################################################################################################

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

########################################################################################################################

# LANGUAGE SETTINGS

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

########################################################################################################################

# FOR FILES

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/STATIC/'
STATICFILES_DIRS = [BASE_DIR / "STATIC"]

MEDIA_ROOT = '/MEDIA/'
MEDIA_ROOT = os.path.join(BASE_DIR, "MEDIA")

########################################################################################################################

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

########################################################################################################################

# CACHE SETTINGS

# FIXME
# CACHES = {
#     'default': {
#         'TIMEOUT': 60,
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': os.path.join(BASE_DIR, 'CACHE_FILES'),
#     }
# }

########################################################################################################################

# ISSUES NOTIFICATION

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple_0': {
            "format": "[{asctime}], [{levelname}], [{message}]",
            "style": "{",
        },
        'simple_1': {
            "format": "[{asctime}], [{levelname}], [{module}], [{message}]",
            "style": "{",
        },
        'simple_2': {
            "format": "[{asctime}], [{levelname}], [{message}], [{pathname}]",
            "style": "{",
        },
        'simple_3': {
            "format": "[{asctime}], [{levelname}], [{message}], [{pathname}], [{exc_info}]",
            "style": "{",
        },
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'console_I': {  # WORKING ONLY ON DEBUG = False
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'simple_1',
            'filters': ['require_debug_false'],
        },
        'console_D': {  # WORKING ONLY ON DEBUG = True
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple_0',
            'filters': ['require_debug_true'],
        },
        'console_W': {  # WORKING ONLY ON DEBUG = True
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple_2',
            'filters': ['require_debug_true'],
        },
        'console_E_C': {  # WORKING ONLY ON DEBUG = True
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple_3',
            'filters': ['require_debug_true'],
        },
        'console_E_C_TO_F': {  # WORKING EVERY
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'simple_3'
        },
        'security': {  # WORKING EVERY
            # 'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'simple_1'
        },
        'mail_001': {  # WORKING ONLY ON DEBUG = False
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'simple_2',
            'filters': ['require_debug_false'],
            # "include_html": True  # If you need html problem type
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console_I', 'console_D', 'console_W', 'console_E_C'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console_E_C_TO_F', 'mail_001'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['console_E_C_TO_F', 'mail_001'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['console_E_C_TO_F'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console_E_C_TO_F'],
            'propagate': True,
        },
    }
}

########################################################################################################################

# EMAIL SETTINGS

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_FORMS = {"signup": "FUNC.forms.CustomForm"}

LOGIN_REDIRECT_URL = "board"
ACCOUNT_LOGOUT_REDIRECT_URL = "board"

########################################################################################################################

# SMTP SETTINGS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # FOR TESTING #
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # FOR REAL TESTING #
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "ljofe@yandex.ru"
EMAIL_HOST_PASSWORD = 'vnrodqfqorptmsxh'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = "ljofe@yandex.ru"

########################################################################################################################

# SEND TO (SETTINGS)

EMAIL_SUBJECT_PREFIX = "NOTIFICATION"
SERVER_EMAIL = "ljofe@yandex.ru"
ADMINS = (
    ('Admin', 'jofeleonids00@gmail.com'),
)

########################################################################################################################
