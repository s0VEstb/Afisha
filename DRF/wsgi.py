"""
WSGI .env for DRF project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import dotenv
from django.core.wsgi import get_wsgi_application

# Determine the base directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the .env file
dotenv.read_dotenv(os.path.join(base_dir, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF.settings')

application = get_wsgi_application()