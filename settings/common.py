"""
Settings located in the folder should be generic between
all system environments (live, staging and dev).

Settings which are specific for an environment should be
withing the specified environment settings file.
"""
import sys
import os

from django.conf.global_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

# Add apps folder to path to allow for better portability whilst developing
sys.path.append(os.path.join(PROJECT_DIR, 'apps'))
sys.path.append(os.path.join(PROJECT_DIR, 'installed_apps'))

# Time zone and internationalisation
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE='en'

ALLOWED_HOSTS = []
SITE_ID=1

# ===================
# Project settings
# ===================

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'conf.wsgi.application'
STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

# Django authentication framework params 
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static_dev'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)


# Application definition
APPS = tuple(os.listdir(os.path.join(PROJECT_DIR, 'apps')))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

INSTALLED_APPS += APPS

#=============
# Addition middleware classes
#=============
MIDDLEWARE_CLASSES += (

)

