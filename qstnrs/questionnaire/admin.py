from questionnaire.models import Questionnaire
from questionnaire.models import Page
from questionnaire.models import Answer
from questionnaire.models import Question
from questionnaire.models import Result
from django.contrib import admin

admin.site.register(Questionnaire)
admin.site.register(Page)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Result)
