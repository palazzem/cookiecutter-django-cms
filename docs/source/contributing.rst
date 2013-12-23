============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

Add new templates
-----------------

If you want to add your bootstrap template, simply submit a pull request:

* Add your template in ``templates`` folder
* In ``base.py`` add your template name in ``CMS_TEMPLATES``
* Add your name in ``AUTHORS.rst`` under ``Contributors`` list

.. note::
   It's better to provide generic templates that could be customized by end users. Don't put your already customized
   template or third party template with Copyright license.

More deployment options
-----------------------

Submit a pull request and edit all required settings to provide new deployment platforms. Be sure to:

* Add a deployment option in ``cookiecutter.json``
* Use ``{% if ... %}`` blocks in settings files
* Add deployment instructions in ``deployment.rst``
