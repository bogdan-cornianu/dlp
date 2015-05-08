#!/bin/sh
coverage run --source='.' manage.py test questionnaire
coverage report
