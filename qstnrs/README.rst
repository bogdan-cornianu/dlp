=====
Questionnaire
=====

A simple questionnaire app.

Quick start
------------
1. Add "qstnrs" to INSTALLED_APPS in settings.py

2. Include qstnrs URLconf in urls.py:
    url(r'^myblog/', include('qstnrs.urls'))

3. Run 'python manage.py syncdb' to create the qstnrs models

4. Run 'python manage.py runserver' to start the development server and access
    http://127.0.0.1:8000/admin to manage questionnaires

5. Access http://127.0.0.1:8000/qstnrs/ to view a list of available questionnaires


-- Dump data from production to test db --
python manage.py dumpdata --natural --exclude auth.permission --exclude contenttypes --indent 4
