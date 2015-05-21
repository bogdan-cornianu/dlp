from django.conf.urls import patterns, url


urlpatterns = patterns(
    'questionnaire.views',
    url(r'^$', 'index', name='qstnrs-index'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<page_id>\d+)/$', 'page',
        name='qstnrs-page'),
    url(r'^(?P<questionnaire_id>\d+)/$', 'page_without_id',
        name='qstnrs-page-no-id'),
    url(r'^result/(?P<questionnaire_id>\d+)/$', 'result', name='qstnrs-result')
)
