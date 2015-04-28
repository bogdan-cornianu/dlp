from questionnaire.models import Questionnaire
from questionnaire.models import Page
from questionnaire.models import Answer
from questionnaire.models import Question
from questionnaire.models import Result
from django.contrib import admin


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('questionnaire_name', 'questionnaire_description')
    search_fields = ('questionnaire_name', 'questionnaire_description')


class PageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'questionnaire')
    search_fields = ('page_name',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'page', 'question_order')
    fields = ('question_text', 'question_order', 'page', 'answers')
    search_fields = ('question_text',)
    filter_horizontal = ('answers',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'answer_score')
    search_fields = ('answer_text',)
    list_filter = ('answer_score',)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('questionnaire', 'page', 'question', 'answer',
                    'session_id')
    search_fields = ('questionnaire', 'page', 'question', 'answer',
                    'session_id')


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
