from questionnaire.models import *
from django.http import HttpResponseRedirect
from questionnaire.forms import PageForm
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
            cleaned_data = form.cleaned_data
            # current_page_index = page_list.index(int(page_id))
            if 'pages' in request.session:
                request.session['pages'] += [cleaned_data]
            else:
                request.session['pages'] = [cleaned_data]
            # print 'Data in session: ', request.session['pages']
            # request.session['previous_page'] = page_id

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
    questionnaire_score = get_score_for(questionnaire_id,
                                        request.session['pages'])
    score_categories = get_categories_for_score(questionnaire_score,
                                                questionnaire_id)
    different_score, different_choices = compute_result(questionnaire_id,
                                                    request.session['pages'])
    del request.session['pages']
    return render(request, "result.html", {
            "score": questionnaire_score,
            "categories": score_categories,
            "different_score": different_score,
            "different_choices": different_choices
    })


def get_categories_for_score(score, questionnaire_id):
    categories = Result.objects.filter(questionnaire_id=questionnaire_id,
                                       lower_limit__lt=score,
                                       upper_limit__gt=score)
    return categories


def get_score_for(questionnaire_id, pages_list):
    score = 0
    for page in pages_list:
        for question_id in page:
            for answer_id in page[question_id]:
                score += Answer.objects.get(id=int(answer_id)).answer_score
    return score


def compute_result(questionnaire_id, pages_list):
    # user_score = get_score_for(questionnaire_id, pages_list)
    better_score = 0
    result = []
    for page in pages_list:
        choice_score, answers_list = question_min_unselected_answers_for(page)
        result.append(answers_list)
        better_score += choice_score
        # print "Q: ", question_id, " Score: ", choice_score

    return better_score, result


def question_min_unselected_answers_for(page):
    min_choice_question = int(page.keys()[0][9:])
    questions = Question.objects.all()
    # print 'min choice question: ', min_choice_question
    for question in page:
        question_id = int(question[9:])
        choices = len(get_choices_for(question_id))
        selected_choices = len(page[question])
        unselected_choices = (choices - selected_choices)

        if unselected_choices < min_choice_question:
            min_choice_question = question_id
    question_text = questions.get(id=min_choice_question)
    selected_choices = page['question_' + str(min_choice_question)]

    return (unselected_score(min_choice_question, selected_choices),
    {question_text: unselected_answers(min_choice_question, selected_choices)})
    # return min_choice_question, unselected_answers(min_choice_question,
    #                                                page[min_choice_question])


def get_choices_for(question_id):
    return [answer.id for answer in
            Question.objects.get(id=question_id).answer_set.all()]


def unselected_answers(question_id, selected_choices):
    print 'uinselect answ: ', question_id
    all_choices = get_choices_for(question_id)
    selected_choices = map(int, selected_choices)

    return list(set(all_choices) - set(selected_choices))


def unselected_score(question_id, selected_choices):
    unselected_score = 0
    all_choices = get_choices_for(question_id)
    selected_choices = map(int, selected_choices)

    unselected_choices = list(set(all_choices) - set(selected_choices))

    for choice_id in unselected_choices:
        unselected_score += Question.objects.get(
                id=question_id).answer_set.get(id=choice_id).answer_score
    return unselected_score


def can_move_to_page(page_index, current_page_index, page_list):
    pass
