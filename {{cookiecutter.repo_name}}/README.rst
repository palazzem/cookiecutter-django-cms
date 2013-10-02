===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.png
    :target: http://badge.fury.io/py/{{ cookiecutter.repo_name }}

.. image:: https://pypip.in/d/{{ cookiecutter.repo_name }}/badge.png
        :target: https://crate.io/packages/{{ cookiecutter.repo_name }}?version=latest


{{ cookiecutter.project_short_description}}

* Free software: BSD license

Requirements
------------

* Django 1.5+
* Python 2.7
* `django-cms`_ 3.0.0.beta2

.. _django-cms: https://github.com/divio/django-cms/tree/3.0.0.beta2

Installation
------------

Enter inside ``{{ cookiecutter.repo_name }}`` folder and install all requirements inside a virtualenv:

.. code-block:: python

    pip install -r requirements/development.txt

Prepare your database (sqlite as default) and run the server:

.. code-block:: python

    python manage.py syncdb --all --settings={{ cookiecutter.repo_name }}.settings.dev
    python manage.py migrate --fake --settings={{ cookiecutter.repo_name }}.settings.dev
    python manage.py cms check --settings={{ cookiecutter.repo_name }}.settings.dev
    python manage.py runserver --settings={{ cookiecutter.repo_name }}.settings.dev

Create your first page with Django CMS admin (``http://localhost:8000/admin``)!

Features
--------

TODO
