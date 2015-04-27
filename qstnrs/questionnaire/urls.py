from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'questionnaire.views',
    url(r'^$', 'index'),
    url(r'^(?P<questionnaire_id>\d+)/$', 'pages'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<page_id>\d+)/$', 'questions'),
    url(r'^(?P<questionnaire_id>\d+)/submit/$', 'submit_questionnaire'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<page_id>\d+)/(?P<question_id>\d+)/$',
        'answers')
)
