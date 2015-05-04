from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

# url(r'^(?P<questionnaire_id>\d+)/$', 'pages'),
# url(r'^(?P<questionnaire_id>\d+)/(?P<page_id>\d+)/(?P<question_id>\d+)/$',
#    'answers')
# url(r'^(?P<questionnaire_id>\d+)/submit/$', 'submit_page'))

urlpatterns = patterns(
    'questionnaire.views',
    url(r'^$', 'index'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<page_id>\d+)/$', 'page'),
    url(r'^result/(?P<questionnaire_id>\d+)/$', 'result')
)
