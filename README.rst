=======================
cookiecutter-django-cms
=======================

`Cookiecutter`_ template for django-cms.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Notes
-----
This project aims to deliver `Django CMS`_ very quickly. Without do anything else which is not already written
in this document, you can use all Django CMS features with just few configurations (4 commands!).
Obviously all these steps follow the `official documentation`_ (beta version) of Django CMS. Remember to read all main
documentation sections because this is **just** a template and there is **NO intention** to replace the original
documentation.

.. _Django CMS: https://www.django-cms.org/en/
.. _official documentation: http://docs.django-cms.org/en/develop/index.html

Usage
-----

If you want to create a personal website using Django CMS but you don't want to create or edit (again) your configuration
files, you can use `Cookiecutter`_ to do all the work.

First, get cookiecutter::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/emanuele-palazzetti/cookiecutter-django-cms.git

You'll be prompted for some questions, answer them, then it will create your CMS.

Features
--------

* Simple Bootstrap 3 template

Basic configurations
--------------------

This template is based on original getting started guide. You have already configured many Django CMS plugins which
you can enable/disable inside ``django_cms/settings/base.py`` with ``INSTALLED_APPS`` setting. There you can also add
more languages (``LANGUAGES``) and templates (``CMS_TEMPLATES``).

If you add or edit a template, remember to add or edit template name inside ``templates`` folder.

More configurations
-------------------

Check original `documentation`_.

.. _documentation: http://docs.django-cms.org/en/develop/getting_started/configuration.html

Other Django CMS bootstrap tools
--------------------------------

* `aldryn-installer`_ from `@nephila`_

.. _aldryn-installer: https://github.com/nephila/aldryn-installer
.. _@nephila: http://twitter.com/NephilaIt

Roadmap
-------

* Heroku deploy (with Amazon S3 for statics)
* Webfaction deploy
* Advanced bootstrap templates

Credits
-------

* `@pydanny`_ and `@audreyr`_ for all their advices in "Two scoops of Django" book
* All `Divio`_ team for this great CMS

.. _@pydanny: http://twitter.com/pydanny
.. _@audreyr: http://twitter.com/audreyr
.. _Divio: https://www.divio.ch/
