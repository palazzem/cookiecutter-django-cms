==========
Deployment
==========

Prepare your git repository
---------------------------

Before continue, be sure to create your git repository::

    $ git init
    $ git add .
    $ git commit -m"Initial commit"

.. note::
   Generated project already have a valid ``.gitignore`` for Django

Heroku
------

If you choose to enable Heroku deployment during project bootstrap, you already have anything you need.
Simply obtain `Heroku Toolbelt`_ and start creating your first application::

    $ heroku apps:create <app_name>
    $ git push heroku master

You have deployed your website in Heroku platform but you need to achieve some extra steps.

.. note::
   Check ``ALLOWED_HOSTS`` setting or you will get a 400 (bad request) error when in production

.. _Heroku Toolbelt: https://toolbelt.heroku.com/

Heroku configuration
--------------------

Set these enviroment variables so production configuration will work like expected::

    $ heroku config:set DJANGO_SECRET_KEY=<random secret key>
    $ heroku config:set DJANGO_SETTINGS_MODULE=django_cms.settings.production

.. note::
   ``django_cms`` package could have a different name according to your initial choose

Configure your `AWS bucket`_ and add these environment variables to Heroku::

    $ heroku config:set AWS_ACCESS_KEY_ID=<random key_id>
    $ heroku config:set AWS_SECRET_ACCESS_KEY=<random access_key>
    $ heroku config:set AWS_STORAGE_BUCKET_NAME=<your bucket name>

.. _AWS bucket: http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html

Syncdb and collect static
-------------------------

Run these commands using Heroku ``run``::

    $ heroku run python django_cms/manage.py syncdb --all
    $ heroku run python django_cms/manage.py migrate --fake
    $ heroku run python django_cms/manage.py collectstatic

.. note::
   ``django_cms`` package could have a different name according to your initial choose

That's all! Your Django CMS website is deployed on Heroku platform!
