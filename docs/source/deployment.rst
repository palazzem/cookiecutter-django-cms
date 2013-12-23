==========
Deployment
==========

Heroku
------

If you choose to enable Heroku deployment during project startup, you already have anything you need.
Simply obtain `Heroku Toolbelt`_ and start creating your first application::

    $ heroku apps:create <my_app_name>
    $ git push heroku

Thats all. You have deployed your website in Heroku platform but you need to achieve some extra steps.

.. _Heroku Toolbelt: https://toolbelt.heroku.com/

Heroku configuration
--------------------

You should set some enviroment variables so production configuration work like expected::

    $ heroku config:set DJANGO_SECRET_KEY=<random secret key>
    $ heroku config:set DJANGO_SETTINGS_MODULE=django_cms.settings.production

.. note::
   ``django_cms`` package could have a different name according to your initial choose

Then configure your `AWS bucket`_ and add these environment variables to Heroku::

    $ heroku config:set AWS_ACCESS_KEY_ID=<random key_id>
    $ heroku config:set AWS_SECRET_ACCESS_KEY=<random access_key>
    $ heroku config:set AWS_STORAGE_BUCKET_NAME=<your bucket name>

.. _AWS bucket: http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html

Syncdb and collect static
-------------------------

Run these commands using Heroku shell::

    $ heroku run python django_cms/manage.py syncdb --all
    $ heroku run python django_cms/manage.py migrate --fake
    $ heroku run python django_cms/manage.py collectstatic

.. note::
   ``django_cms`` package could have a different name according to your initial choose
