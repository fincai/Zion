"""
WSGI config for zion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""


import os
import sys

#sys.path.append('/Library/WebServer/Documents/zion/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zion.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
