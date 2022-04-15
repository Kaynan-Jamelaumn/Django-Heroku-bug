import environ

from store.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEUBG", False)

SECRET_KEY = env("SECRET_KEY")
"""
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
"""

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""
DATABASES = {
    'default': env.db(),


}
