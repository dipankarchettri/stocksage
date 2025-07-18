"""
WSGI config for stocksage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


settings_module = 'api.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'api.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocksage.settings')

application = get_wsgi_application()
