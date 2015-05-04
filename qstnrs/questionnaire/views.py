from questionnaire.models import Questionnaire, Question, Page
from questionnaire.forms import PageForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
    questionnaires = []
    for questionnaire in Questionnaire.objects.all():
        pages = Page.objects.select_related('questionnaire_id').\
            filter(questionnaire_id=questionnaire.id).order_by('page_order')

        if len(pages) > 0:
            first_page_id = pages[0].id

        questionnaires.append({
            'name': questionnaire.questionnaire_name,
            'description': questionnaire.questionnaire_description,
            'id': questionnaire.id,
            'page_list': [page.id for page in pages],
            'first_page_id': first_page_id
        })
    request.session['page_id'] = first_page_id
    return render(request, "main.html",
                  {"questionnaire_list": questionnaires})


def page(request, questionnaire_id, page_id):
    questions = Question.objects.\
                    select_related('questionnaire_id').filter(page_id=page_id)
    ordered_pages = Page.objects.filter(questionnaire_id=questionnaire_id).\
                                                        order_by('page_order')
    page_list = [page.id for page in ordered_pages]

    current_page = get_object_or_404(Page, questionnaire_id=questionnaire_id,
                                    id=page_id)
    previous_page = page_list[page_list.index(int(page_id)) - 1]
    if previous_page == page_list[-1]:
        previous_page = 0
    try:
        next_page = page_list[page_list.index(int(page_id)) + 1]
    except IndexError:
        next_page = -1

    if 'previousPage' in request.POST:
        goto_page = previous_page
    elif 'nextPage' in request.POST:
        goto_page = next_page
    elif 'viewResults' in request.POST:
        return HttpResponseRedirect('/qstnrs/result/' + questionnaire_id)

    if request.method == 'POST':
        form = PageForm(request.POST, page=current_page)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            return HttpResponseRedirect('/qstnrs/' + questionnaire_id + '/' +
                                        str(goto_page))
    else:
        form = PageForm(page=current_page)

    return render(request, "page.html", {
                    "form": form,
                    "questions_list": questions,
                    "previous_page_index": previous_page,
                    "next_page_index": next_page,
                    "questionnaire_id": questionnaire_id
    })


def result(request, questionnaire_id):
    return HttpResponse("MAMA")
