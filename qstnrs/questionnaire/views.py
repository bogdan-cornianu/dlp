from questionnaire.models import *
from questionnaire.forms import PageForm
from questionnaire.utils import get_score_for, get_categories_for_score,\
                                get_minimal_better, get_minimal_worse
from django.http import HttpResponseRedirect
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
    previous_page_id = page_list[page_list.index(int(page_id)) - 1]

    if previous_page_id == page_list[-1]:
        previous_page_id = 0
    try:
        next_page_id = page_list[page_list.index(int(page_id)) + 1]
    except IndexError:
        next_page_id = -1

    if request.method == 'POST':
        form = PageForm(request.POST, page=current_page)
        if form.is_valid():
            if 'choices' not in request.session:
                request.session['choices'] = []
            request.session['choices'] += [int(id)
                                        for value in form.cleaned_data.values()
                                        for id in value]

            if 'previousPage' in request.POST:
                goto_page = previous_page_id
            elif 'nextPage' in request.POST:
                goto_page = next_page_id
            elif 'viewResults' in request.POST:
                return HttpResponseRedirect('/qstnrs/result/' +
                                            questionnaire_id)

            return HttpResponseRedirect('/qstnrs/' + questionnaire_id + '/' +
                                        str(goto_page))
    else:
        form = PageForm(page=current_page)
    return render(request, "page.html", {
            "form": form,
            "questions_list": questions,
            "previous_page_id": previous_page_id,
            "next_page_id": next_page_id,
            "questionnaire_id": questionnaire_id
    })


def result(request, questionnaire_id):
    user_choices = request.session['choices']
    user_score = get_score_for(user_choices)
    score_categories = get_categories_for_score(user_score, questionnaire_id)

    minimal_better = get_minimal_better(int(questionnaire_id),
                                        map(int, user_choices))
    minimal_worse = get_minimal_worse(int(questionnaire_id),
                                      map(int, user_choices))

    # user_choices = [2, 5, 10, 14, 17, 20, 23, 27]
    # unselected_choices = [1, 3, 4, 6, 7, 8, 9, 11, 12, 13, 15, 16, 18,
    #                                19, 21, 22, 24, 25, 26]
    # unselected = Answer.objects.filter(id__in=unselected_choices)
    # print 'worse: ',select_optimal_answers(1, user_choices, unselected, better=False)

    del request.session['choices']
    return render(request, "result.html", {
            "score": user_score,
            "categories": score_categories,
            "minimal_better": minimal_better,
            "minimal_worse": minimal_worse
    })
