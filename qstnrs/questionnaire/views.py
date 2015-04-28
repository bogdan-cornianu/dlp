from questionnaire.models import Questionnaire, Question, Page
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    questionnaires = []
    for questionnaire in Questionnaire.objects.all():
        pages = Page.objects.select_related('questionnaire_id').\
            filter(questionnaire_id=questionnaire.id)

        if len(pages) > 0:
            first_page_id = pages[0].id

        questionnaires.append({
            'name': questionnaire.questionnaire_name,
            'description': questionnaire.questionnaire_description,
            'id': questionnaire.id,
            'first_page_id': first_page_id
        })
    return render(request, "index.html",
                  {"questionnaire_list": questionnaires})


def pages(request, questionnaire_id):
    pages_list = Page.objects.filter(questionnaire_id=questionnaire_id)
    return render(request, "pages.html",
                  {"pages": pages_list, "questionnaire_id": questionnaire_id})


def questions(request, questionnaire_id, page_id):
    questions = Question.objects.\
                    select_related('questionnaire_id').filter(page_id=page_id)
    pages_list = Page.objects.filter(questionnaire_id=questionnaire_id)
    return render(request, "questions.html",
                  {"questions_list": questions, "pages": pages_list,
                   "questionnaire_id": questionnaire_id})


def answers(request, questionnaire_id, page_id, question_id):
    return HttpResponse("Answers"
                        + " for question " + str(question_id)
                        + " of page " + str(page_id)
                        + " from questionnaire " + str(questionnaire_id))


def submit_page(request, questionnaire_id):
    pass
