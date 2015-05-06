from questionnaire.models import Answer, Question, Result


def get_score_for(choices):
    score = 0
    for choice_id in choices:
        score += Answer.objects.get(id=choice_id).answer_score

    return score


def get_categories_for_score(score, questionnaire_id):
    categories = Result.objects.filter(questionnaire_id=questionnaire_id,
                                       lower_limit__lt=score,
                                       upper_limit__gt=score)
    return categories


'''
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
    score = 0
    result = []
    for page in pages_list:
        choice_score, answers_list = question_min_unselected_answers_for(page)
        if len(answers_list) > 0:
            result.append(answers_list)
        score += choice_score

    return score, result


def question_min_unselected_answers_for(page):
    # get the first question on the page as a seed
    min_choice_question = int(page.keys()[0][9:])
    questions = Question.objects.all()

    # find the question with the minimum unselected choices
    for question in page:
        question_id = int(question[9:])
        choices = len(get_choices_for(question_id))
        selected_choices = len(page[question])
        unselected_choices = (choices - selected_choices)

        if unselected_choices < min_choice_question:
            min_choice_question = question_id

    question_text = questions.get(id=min_choice_question)
    selected_choices = page['question_' + str(min_choice_question)]

    questions_and_answers = {}
    unselected = unselected_answers(min_choice_question, selected_choices)

    # don't add questions with no answers
    if len(unselected) > 0:
        questions_and_answers[question_text] = unselected

    return (unselected_score(min_choice_question, selected_choices),
            questions_and_answers)


def get_choices_for(question_id):
    return [answer.id for answer in
            Question.objects.get(id=question_id).answer_set.all()]


def unselected_answers(question_id, selected_choices):
    all_choices = get_choices_for(question_id)
    selected_choices = map(int, selected_choices)
    unselected_choices = list(set(all_choices) - set(selected_choices))

    return map(lambda x: Answer.objects.get(id=x, question_id=question_id),
               unselected_choices)


def unselected_score(question_id, selected_choices):
    unselected_score = 0
    all_choices = get_choices_for(question_id)
    selected_choices = map(int, selected_choices)

    unselected_choices = list(set(all_choices) - set(selected_choices))

    for choice_id in unselected_choices:
        unselected_score += Question.objects.get(
                id=question_id).answer_set.get(id=choice_id).answer_score
    return unselected_score
'''
