from .base import *
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["joel20.pythonanywhere.com"]

# to disable the the console.log on browser
PWA_APP_DEBUG_MODE = False

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.mysql',
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "NAME": os.getenv("DB_NAME"),
    }
}
