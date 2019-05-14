"""
WSGI config for web_hw3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
# 打包部署
# import os
# from django.core.wsgi import get_wsgi_application
# import django
# import sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, BASE_DIR)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_hw3.settings')
# django.setup()
# application = get_wsgi_application()

# 本地
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_hw3.settings")

application = get_wsgi_application()
