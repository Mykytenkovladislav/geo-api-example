"""
This file contains all the settings that defines the development server.
SECURITY WARNING: don't run with debug turned on in production!
"""

from core.settings.components import BASE_DIR
from core.settings.components.base import env, MIDDLEWARE, INSTALLED_APPS

DEBUG = env("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = ["*"]

# Security
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
CORS_ORIGIN_ALLOW_ALL = True

STATIC_ROOT = BASE_DIR.joinpath("..", "staticfiles")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"


DOMAIN = "localhost"
SCHEMA = "http"
