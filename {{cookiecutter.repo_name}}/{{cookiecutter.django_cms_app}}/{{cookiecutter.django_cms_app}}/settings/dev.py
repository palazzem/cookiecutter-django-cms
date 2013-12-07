from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{{cookiecutter.repo_name}}.db',
    }
}

SECRET_KEY = 'devel'
