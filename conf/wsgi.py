"""
WSGI config for testing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import envvars

envvars_file = os.path.join('env')
if os.path.exists(envvars_file):
    envvars.load(envvars_file)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
