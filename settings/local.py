"""
	Local development settings, used when using runserver
"""

from settings.common import *

# Enter a sectret key
SECRET_KEY = 'SECRET_KEY'

DEBUG = True

TEMPLATE_DEBUG = DEBUG


ADMINS = (
    ('name', 'name@email'),
)
MANAGER = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'dev.db'),
    }
}
