Questionnaire
=============

A Django application where authenticated users can create questionnaires that can be filled in by
unauthenticated users.

Quick start
-----------
1. Install the Questionnaire egg file by running:
    easy_install Questionnaire.egg

2. Add "questionnaire" to INSTALLED_APPS in settings.py

3. Include questionnaire URLconf in urls.py:
    url(r'^myblog/', include('questionnaire.urls'))

4. Run 'python manage.py syncdb' to create the questionnaire models

5. Run 'python manage.py runserver' to start the development server and access
    http://127.0.0.1:8000/admin to manage questionnaires

6. Access http://127.0.0.1:8000/questionnaire/ to view a list of available questionnaires

