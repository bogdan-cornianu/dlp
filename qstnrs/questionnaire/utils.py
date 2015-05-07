from questionnaire.models import Answer, Question, Result


def get_score_for(user_choices):
    score = 0
    for choice_id in user_choices:
        score += Answer.objects.get(id=choice_id).answer_score

    return score


def get_categories_for_score(score, questionnaire_id):
    categories = Result.objects.filter(questionnaire_id=questionnaire_id,
                                       lower_limit__lt=score,
                                       upper_limit__gt=score)
    return categories


def get_minimal_better(questionnaire_id, user_choices):
    # only get the answers for the current questionnaire
    available_answers = [answer for answer in Answer.objects.all()
                if answer.question.page.questionnaire.id == questionnaire_id]

    unselected_choices = []
    for choice in available_answers:
        if choice.answer_score > 0 and choice.id not in user_choices:
            unselected_choices.append(choice)
    unselected_choices.sort(key=lambda a: a.answer_score, reverse=True)

    return select_optimal_answers(questionnaire_id, unselected_choices)


def get_minimal_worse(questionnaire_id, user_choices):
    # only get the answers for the current questionnaire
    available_answers = [answer for answer in Answer.objects.all()
                if answer.question.page.questionnaire.id == questionnaire_id]

    # get only negative, unselected answers and sort them ascending by score
    unselected_choices = [a for a in available_answers
                        if a.answer_score < 0
                        and a.id not in user_choices]\
                        .sort(key=lambda a: a.answer_score)

    return select_optimal_answers(questionnaire_id, unselected_choices)


def select_optimal_answers(questionnaire_id, unselected_choices):
    user_score = get_score_for([a.id for a in unselected_choices])
    user_categories = get_categories_for_score(user_score, questionnaire_id)

    possible_answers = []
    upper_limit = get_closest_upper_limit(user_categories, user_score)
    gap = upper_limit - user_score

    for choice in unselected_choices:
        if gap > 0:
            if not on_same_page(choice, unselected_choices):
                possible_answers.append(choice)
                gap -= abs(choice.answer_score)
        else:
            break

    # remove answers of questions from the same page
    # going from the lowest score answer, eliminate it from the result list
    # if there is another answer with the same page id
    # for a in possible_answers:
    #     if [pid.question.page.id for pid in possible_answers].count(a.question.page.id) > 1\
    #     and [qid.question.id for qid in possible_answers].count(a.question.id) == 1:
    #         del possible_answers[possible_answers.index(a)]


    # eliminate answers from different questions on the same page

    return possible_answers


def get_closest_upper_limit(categories, user_score):
    closest_limit = categories[0].upper_limit
    for c in categories:
        if c.upper_limit > user_score and c.upper_limit < closest_limit:
            closest_limit = c.upper_limit

    return closest_limit


def on_same_page(answer, possible_choices):
    for choice in possible_choices:
        if choice.question.id != answer.question.id\
        and choice.question.page.id == answer.question.page.id:
            return True
    return False

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
