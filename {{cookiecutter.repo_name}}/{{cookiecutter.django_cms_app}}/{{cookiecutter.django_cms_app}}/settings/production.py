from .base import *

DEBUG = environ.get('DJANGO_DEBUG', False)
TEMPLATE_DEBUG = DEBUG

SITE_ID = 2

{% if cookiecutter.heroku == "y" or cookiecutter.heroku == "Y" %}
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = [
    '{{ cookiecutter.site_name }}',
]

INSTALLED_APPS += (
    'storages',
)

# Amazon S3 credentials
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Static files location
from S3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL
MEDIA_URL = S3_URL
{% endif %}
