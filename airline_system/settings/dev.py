import os
from .common import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")


SECRET_KEY = os.environ.get("SECRET_KEY")

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
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}
database_url = os.environ.get("DATABASE_URL")
DATABASES["default"] = dj_database_url.parse(database_url)
