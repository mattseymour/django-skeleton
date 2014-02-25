django-skeleton - Django Skeleton
===============

Django Skeleton provides a skeleton project setup for django (kind of in the name isnt it).

Features include:
 - Multiple settings files inherited from a common settings file for each of your environments (if using environment variables just add settings.local for development in your bash file `export DJANGO_SETTINGS_MODULE='settings.local'`), 
 - Auto includition of projects added to `apps` directory
 - Improved layout on the original django project layout

=== Notes ===
- Within each settings file you will need to specify a SECRET_KEY (which is a 50 character long random string).

This application has only been written so please state any issues you might have and I will aim to sort them out as soon as possible.
