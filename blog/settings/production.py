from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.mysql',
        "HOST": "localhost",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "Root@44223",
        "NAME": "blog_info",
    }
}
