from questionnaire.models import Questionnaire, Question, Page
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    questionnaires = []
    for questionnaire in Questionnaire.objects.all():
        questionnaires.append({
            'name': questionnaire.questionnaire_name,
            'description': questionnaire.questionnaire_description,
            'id': questionnaire.id,
            'first_page_id': Page.objects.select_related('questionnaire_id').
            filter(questionnaire_id=questionnaire.id)[0].id
        })
    template = loader.get_template("index.html")
    context = Context({
        "questionnaire_list": questionnaires
    })
    return HttpResponse(template.render(context))


def pages(request, questionnaire_id):
    pages_list = Page.objects.filter(questionnaire_id=questionnaire_id)
    template = loader.get_template("pages.html")
    context = Context({
        "pages": pages_list,
        "questionnaire_id": questionnaire_id
    })
    return HttpResponse(template.render(context))


def questions(request, questionnaire_id, page_id):
    questions = Question.objects.\
                    select_related('questionnaire_id').filter(page_id=page_id)
    pages_list = Page.objects.filter(questionnaire_id=questionnaire_id)
    template = loader.get_template("questions.html")
    context = Context({
        "questions_list": questions,
        "pages": pages_list,
        "questionnaire_id": questionnaire_id
    })
    return HttpResponse(template.render(context))


def answers(request, questionnaire_id, page_id, question_id):
    return HttpResponse("Answers"
                        + " for question " + str(question_id)
                        + " of page " + str(page_id)
                        + " from questionnaire " + str(questionnaire_id))


def submit_questionnaire(request, questionnaire_id):
    pass
