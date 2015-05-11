from questionnaire.models import *
from questionnaire.forms import PageForm
from questionnaire.utils import get_score_for, get_categories_for_score, \
    get_minimal_better, get_minimal_worse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    paginator = Paginator(Questionnaire.objects.all(), 3)
    questionnaire_page = request.GET.get('page')

    try:
        questionnaires = paginator.page(questionnaire_page)
    except PageNotAnInteger:
        questionnaires = paginator.page(1)
    except EmptyPage:
        questionnaires = paginator.page(paginator.num_pages)

    return render(request, "main.html",
                  {"questionnaires": questionnaires})


def page_without_id(request, questionnaire_id):
    try:
        first_page = Questionnaire.objects.get(id=questionnaire_id).page_set. \
            all()[0].id
        url = '/qstnrs/' + questionnaire_id + '/' + str(first_page)
    except IndexError:
        url = '/qstnrs/'

    return HttpResponseRedirect(url)


def page(request, questionnaire_id, page_id):
    questions = Question.objects. \
        select_related('questionnaire_id').filter(page_id=page_id)
    ordered_pages = Page.objects.filter(questionnaire_id=questionnaire_id). \
        order_by('page_order')
    page_list = [ordered_page.id for ordered_page in ordered_pages]

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
            request.session['choices'] += [int(choice_id)
                                           for value in
                                           form.cleaned_data.values()
                                           for choice_id in value]

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

    del request.session['choices']
    return render(request, "result.html", {
        "score": user_score,
        "categories": score_categories,
        "minimal_better": minimal_better,
        "minimal_worse": minimal_worse
    })
