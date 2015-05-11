from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'questionnaire.views',
    url(r'^$', 'index'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<page_id>\d+)/$', 'page'),
    url(r'^(?P<questionnaire_id>\d+)/$', 'page_without_id'),
    url(r'^result/(?P<questionnaire_id>\d+)/$', 'result')
)
