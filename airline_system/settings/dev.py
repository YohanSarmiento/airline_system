from .common import *

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECRET_KEY = 'django-insecure-(%0n7-yw0lr1f2eav7t(o(&xu102c(ggf##&o)j!@u*o(86rw*'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "airline",
        "USER": "yohan",
        "PASSWORD": "123#yohan",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}