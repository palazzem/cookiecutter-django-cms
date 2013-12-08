============================
Django CMS with Cookiecutter
============================

`Cookiecutter`_ template for django-cms.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Disclaimer
----------

This project aims to deliver `Django CMS`_ very quickly. Without do anything else which is not already written
in this document, you can use all Django CMS features with just few configurations (5 commands!).
Obviously all these steps follow the `official documentation`_ (beta version) of Django CMS. Remember to read all main
documentation sections because this is **just** a template and there is **NO intention** to replace the official
documentation.

.. _Django CMS: https://www.django-cms.org/en/
.. _official documentation: http://docs.django-cms.org/en/develop/index.html

Features
--------

* Simple Bootstrap 3 template
* Heroku fast deploy (with Amazon S3 for statics)

Installation and usage
----------------------

If you want to create a personal website using Django CMS but you don't want to create or edit (again) your configuration
files, you can use `Cookiecutter`_ to do all the work.

First, get cookiecutter::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/emanuele-palazzetti/cookiecutter-django-cms.git

You'll be prompted for some questions (included Heroku deployment settings).
After project generation, you'll find a README.rst in which you'll find all information to sync your database with fake migrations. Before your first commit remember to change (if required) the ``LICENSE`` file.

Now you are ready to use Django CMS!

Basic configurations
--------------------

This template is based on official getting started guide. You have already configured many Django CMS plugins which
you can enable/disable inside ``django_cms/settings/base.py`` with ``INSTALLED_APPS`` setting. There you can also add
more languages (``LANGUAGES``) and templates (``CMS_TEMPLATES``).

If you add or edit a template, remember to add or edit template name inside ``templates`` folder.

More configurations
-------------------

Check official `documentation`_.

.. _documentation: http://docs.django-cms.org/en/develop/getting_started/configuration.html

Other Django CMS bootstrap tools
--------------------------------

* `aldryn-installer`_ from `@nephila`_

.. _aldryn-installer: https://github.com/nephila/aldryn-installer
.. _@nephila: http://twitter.com/NephilaIt

Roadmap
-------

* Webfaction deploy (with nginx frontend to serve statics)
* Advanced bootstrap templates (from Bootstrap example)

Credits
-------

* `@pydanny`_ and `@audreyr`_ for all their advices in "Two scoops of Django" book
* All `Divio`_ team for this great CMS

.. _@pydanny: http://twitter.com/pydanny
.. _@audreyr: http://twitter.com/audreyr
.. _Divio: https://www.divio.ch/
