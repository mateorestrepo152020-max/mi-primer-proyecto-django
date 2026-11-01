"""
WSGI config for mi_primer_proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')

application = get_wsgi_application()
