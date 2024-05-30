import os
from .common import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'django-insecure-(bf5i@@fe0_l$glmjtm$6c&3s17ogzo8bv!azr%*7&#8oxcnmx'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "airline",
#         "USER": "yohan",
#         "PASSWORD": "29475#yohan",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "airline",
        "USER": "yohan",
        "PASSWORD": "29475#yohan",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}