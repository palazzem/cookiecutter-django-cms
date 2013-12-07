web: gunicorn --pythonpath="$PWD/django_cms" django_cms.wsgi:application -t 120 -w 8 -k gevent --max-requests 250
