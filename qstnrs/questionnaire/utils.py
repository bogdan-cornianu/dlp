from questionnaire.models import Answer, Result


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
    available_answers = answers_for_questionnaire(questionnaire_id)

    unselected_choices = sorted([a for a in available_answers
                                 if a.answer_score > 0
                                 and a.id not in user_choices],
                                key=lambda a: a.answer_score, reverse=True)

    return select_optimal_answers(questionnaire_id, user_choices,
                                  unselected_choices,
                                  better=True)


def get_minimal_worse(questionnaire_id, user_choices):
    # only get the answers for the current questionnaire
    available_answers = answers_for_questionnaire(questionnaire_id)

    # get only negative, unselected answers and sort them ascending by score
    unselected_choices = sorted([a for a in available_answers
                                 if a.answer_score < 0
                                 and a.id not in user_choices],
                                key=lambda a: a.answer_score)

    return select_optimal_answers(questionnaire_id, user_choices,
                                  unselected_choices,
                                  better=False)


def select_optimal_answers(questionnaire_id, user_choices,
                           unselected_choices, better):
    user_score = get_score_for(user_choices)
    user_categories = get_categories_for_score(user_score, questionnaire_id)

    possible_answers = []
    if user_categories:
        limit = get_closest_limit(user_categories, user_score, better)
        if better:
            gap = limit - user_score
        else:
            gap = user_score - limit

        for choice in unselected_choices:
            if gap > 0:
                if better:
                    if choice.answer_score < limit - user_score and not on_same_page(choice, possible_answers):
                        possible_answers.append(choice)
                        gap -= abs(choice.answer_score)
                else:
                    if choice.answer_score < user_score - limit and not on_same_page(choice, possible_answers):
                        possible_answers.append(choice)
                        gap -= abs(choice.answer_score)
            else:
                break

        return get_improvements(possible_answers, better)
    return None


def get_closest_limit(categories, user_score, better):
    if better:
        closest_limit = categories[0].upper_limit
    else:
        closest_limit = categories[0].lower_limit
    for c in categories:
        if better:
            if c.upper_limit > user_score and c.upper_limit < closest_limit:
                closest_limit = c.upper_limit
        else:
            if c.lower_limit < user_score and c.lower_limit > closest_limit:
                closest_limit = c.lower_limit

    return closest_limit


def on_same_page(answer, possible_choices):
    for choice in possible_choices:
        if choice.question.id != answer.question.id\
        and choice.question.page.id == answer.question.page.id:
            return True
    return False


def answers_for_questionnaire(questionnaire_id):
    return [answer for answer in Answer.objects.all()
            if answer.question.page.questionnaire.id == questionnaire_id]


def get_improvements(suggested_answers, better):
    improvements = {}

    for answer in suggested_answers:
        question_text = answer.question.question_text
        if question_text in improvements:
            improvements[question_text].append(answer.answer_text)
        else:
            improvements[question_text] = [answer.answer_text]

    return improvements
