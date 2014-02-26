django-skeleton - Django Skeleton
===============

Django Skeleton provides a skeleton project setup for django (kind of in the name isnt it).

Features include:
 - Multiple settings files inherited from a common settings file for each of your environments (if using environment variables just add settings.local for development in your bash file `export DJANGO_SETTINGS_MODULE='settings.local'`), 
 - Auto includition of projects added to `apps` directory
 - Improved layout on the original django project layout

### Getting started
In order to use this template you can either download the source from the github page download link and extract; or, clone the repo.

    git clone https://github.com/mattseymour/django-skeleton.git <projectname>

If using git clone you will then have to remove the git remote to this repo.

    git remote rm origin

    git remote add origin <your-project-repo>

### Notes
- Within each settings file you will need to specify a SECRET_KEY (which is a 50 character long random string).
- If you need to generate a secret key then you can use this script to do it for you. https://gist.github.com/mattseymour/9205591

This application has only been written so please state any issues you might have and I will aim to sort them out as soon as possible.
