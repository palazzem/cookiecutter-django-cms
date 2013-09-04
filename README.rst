Django CMS 3 (beta2) template
=============================

This project aims to deliver `Django CMS`_ very quickly. Without do anything else which is not already written
in this document, you can use all Django CMS features with just few configurations.
Obviously all my steps follow the `official documentation`_ (beta version) of Django CMS. Remember to read all main
documentation sections because this is **just** a template.

.. _Django CMS: https://www.django-cms.org/en/
.. _official documentation: http://docs.django-cms.org/en/develop/index.html

Requirements
------------

* Django 1.5+
* Python 2.7
* `django-cms`_ 3.0.0.beta2

.. _django-cms: https://github.com/divio/django-cms/tree/3.0.0.beta2

Installation
------------

Clone this repository (change project_name with something more suitable for you):

.. code-block:: python

    git clone https://github.com/emanuele-palazzetti/django-cms-template.git project_name

Enter inside ``project_name`` folder and install all requirements:

.. code-block:: python

    pip install -r requirements/development.txt

**NOTE**: from now on, all commands are launched inside ``django_cms`` folder!

Prepare your database (sqlite as default) and create your admin account:

.. code-block:: python

    python manage.py syncdb --all --settings=django_cms.settings.dev
    python manage.py migrate --fake --settings=django_cms.settings.dev

If you follow all steps, you can check your installation with:

.. code-block:: python

    python manage.py cms check --settings=django_cms.settings.dev

To start using Django CMS, just run your server:

.. code-block:: python

    python manage.py runserver --settings=django_cms.settings.dev

and start creating your first page with Django CMS admin (``http://localhost:8000/admin``)!

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

Credits
-------

* `@pydanny`_ and `@audreyr`_ for all their advices in "Two scoops of Django" book
* All `Divio`_ team for this great CMS

.. _@pydanny: http://twitter.com/pydanny
.. _@audreyr: http://twitter.com/audreyr
.. _Divio: https://www.divio.ch/
