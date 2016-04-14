============================
Django CMS with Cookiecutter
============================

A `Cookiecutter`_ template for `django-cms`_ to deliver your website with a strong Django backend.

Documentation: http://cookiecutter-django-cms.rtfd.org

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _django-cms: https://www.django-cms.org/

Features
--------

* Simple Bootstrap 3 templates ready to use
* django compressor included
* Heroku deployment (with Amazon S3 for statics)

Installation and usage
----------------------

If you want to create a personal website using Django CMS but you don't want to create or edit (again) your configuration
files, you can use `Cookiecutter`_ to do all the work.

First, get cookiecutter::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/palazzem/cookiecutter-django-cms

You'll be prompted for some questions (included Heroku deployment settings).
After project generation, you'll find a README.rst in which you'll find all information to sync your database with fake migrations. Before your first commit remember to change (if required) the ``LICENSE`` file.

Now you are ready to use Django CMS!

Basic configurations
--------------------

This template is based on official getting started guide. You have already configured many Django CMS plugins which
you can enable/disable inside ``django_cms/settings/base.py`` with ``INSTALLED_APPS`` setting. There you can also add
more languages (``LANGUAGES``) and templates (``CMS_TEMPLATES``).

More configurations
-------------------

Check official `documentation`_.

.. _documentation: http://django-cms.readthedocs.org/en/develop/reference/configuration.html

Other Django CMS bootstrap tools
--------------------------------

* `aldryn-installer`_ from `@nephila`_

.. _aldryn-installer: https://github.com/nephila/aldryn-installer
.. _@nephila: http://twitter.com/NephilaIt

Roadmap
-------

* Webfaction deploy (with nginx frontend to serve statics)
* More bootstrap templates (single page scroller, etc...)
  
TO DO 
-----

* Update docs

Credits
-------

* `@pydanny`_ and `@audreyr`_ for all their advices in "Two scoops of Django" book
* All `Divio`_ team for this great CMS

.. _@pydanny: http://twitter.com/pydanny
.. _@audreyr: http://twitter.com/audreyr
.. _Divio: https://www.divio.ch/
