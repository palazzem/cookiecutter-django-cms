=====
Usage
=====

Bootstrap your project
----------------------

First, get and install cookiecutter in your virtualenv::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/palazzem/cookiecutter-django-cms.git --checkout 0.2.3

You'll be prompted for some project configurations::

    full_name (default is "Michael Scott")?
    email (default is "bestboss.scott@example.com")?
    github_username (default is "mscott")?
    year (default is "2013")?
    version (default is "0.1.0")?
    project_name (default is "Django CMS")?
    repo_name (default is "django-cms-web")?
    django_cms_app (default is "django_cms")?
    project_short_description (default is "Django CMS boilerplate to start your website in 5 minutes.")?
    languages (default is "en")?
    site_name (default is "example.com")?
    django_filer (default is "n")?
    heroku (default is "y")?

Now you are ready to use Django CMS!

Initial configurations
----------------------

Like any other Django project you should do these extra steps (if you are a Djangonaut, skip this).

Install all development requirements in your virtualenv::

    $ pip install -r requirements/development.txt

Sync your database with migrations::

    $ python manage.py syncdb --all --settings=django_cms.settings.dev
    $ python manage.py migrate --fake --settings=django_cms.settings.dev

Run all Django CMS check and start django runserver::

    $ python manage.py cms check --settings=django_cms.settings.dev
    $ python manage.py runserver --settings=django_cms.settings.dev

Open http://localhost:8000 and create your first page with Django CMS admin!

.. note::
   You can avoid to use ``--settings`` parameter if you export ``DJANGO_SETTINGS_MODULE=django_cms.settings.dev`` in your environment

.. note::
   ``django_cms`` package could have a different name according to your initial choose

More configurations
-------------------

For more Django CMS configurations, check official `documentation`_ (still in beta).

.. _documentation: http://docs.django-cms.org/en/develop/getting_started/configuration.html
