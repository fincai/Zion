"""
Django settings for zion project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(2&*e+7%ks$jd3tfxnt+0!09kl7j7bqq=!wwlg=uzl36ea5n3y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'django_ajax',
    'zion.register',
    'zion.signin',
    'zion.forums',
    'zion.articles',
    'zion.comments',
    'zion.avatar',
    'zion.profiles',
    'zion.popular',
    'zion.tags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zion.urls'

WSGI_APPLICATION = 'zion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zion',
        'USER': 'Farley',
        'PASSWORD': '014216',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''

TEMPLATE_DIRS = (
		os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/'),
)

STATICFILES_DIRS = (
        os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/'),
)

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

# Extended User model
AUTH_USER_MODEL = 'signin.User'

# Upload file size limitation (in bytes)
UPLOAD_LIMIT = 1048576

AVATAR_ROOT = os.path.join(os.path.dirname(__file__), 'static/avatars/').replace('\\', '/')
