from questionnaire.models import *
from questionnaire.forms import PageForm
from questionnaire.utils import get_score_for, get_suggestions_for
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    paginator = Paginator(Questionnaire.objects.all(), 3)
    questionnaire_page = request.GET.get('page')

    if 'choices' in request.session:
        del request.session['choices']

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
        first_page = Page.objects.filter(questionnaire_id=questionnaire_id). \
            order_by('page_order')[0].id
        url = '/qstnrs/' + questionnaire_id + '/' + str(first_page)
    except IndexError:
        url = '/qstnrs/'

    return HttpResponseRedirect(url)


def page(request, questionnaire_id, page_id):
    # Get the list of pages
    page_list = Page.objects.filter(
        questionnaire_id=int(questionnaire_id)
    ).order_by('page_order')
    page_has_questions = Question.objects.filter(
        page_id=int(page_id)
    ).count() > 0

    current_page = get_object_or_404(page_list, id=int(page_id))
    # Get next page id, if there isn't one, display the View Results button
    try:
        next_page_id = page_list.filter(
            page_order__gt=current_page.page_order
        )[0].id
    except IndexError:
        next_page_id = -1
    # Get previous page id, if there isn't one, hide the Previous Page button
    try:
        previous_page_id = page_list.filter(
            page_order__lt=current_page.page_order
        )[0].id
    except IndexError:
        previous_page_id = 0

    if request.method == 'POST':
        form = PageForm(request.POST, page=current_page)
        if form.is_valid():
            if 'choices' not in request.session:
                request.session['choices'] = []
            request.session['choices'] += [
                int(choice_id)
                for value in form.cleaned_data.values()
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
        "page_has_questions": page_has_questions,
        "previous_page_id": previous_page_id,
        "next_page_id": next_page_id,
        "questionnaire_id": questionnaire_id
    })


def result(request, questionnaire_id):
    user_choices = request.session['choices']
    user_score = get_score_for(user_choices)
    better_suggestions = get_suggestions_for(
        int(questionnaire_id), user_choices, better=True
    )
    worse_suggestions = get_suggestions_for(
        int(questionnaire_id), user_choices, better=False
    )
    try:
        questionnaire = Questionnaire.objects.get(
            id=questionnaire_id,
            result_upper_limit__gt=user_score
        )
    except Questionnaire.DoesNotExist:
        questionnaire = None

    del request.session['choices']
    return render(request, "result.html", {
        "user_score": user_score,
        "questionnaire": questionnaire,
        "better_suggestions": better_suggestions,
        "worse_suggestions": worse_suggestions
    })
