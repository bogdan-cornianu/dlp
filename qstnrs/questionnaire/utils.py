from questionnaire.models import Answer


def get_score_for(user_choices):
    """Calculate the user's total score based on selected answers."""
    return sum(list(Answer.objects.filter(id__in=user_choices).values_list(
        'answer_score', flat=True)))


def answers_for_questionnaire(questionnaire_id):
    result = []
    for answer in Answer.objects.all():
        if answer.question.page.questionnaire_id == questionnaire_id:
            result.append(answer)

    return result


def select_optimal_answers(user_choices, unselected_choices, better):
    """Select all the answers the user could have selected for a better or
    worse score.--add order-to-doc"""
    user_score = get_score_for(user_choices)

    possible_answers = []
    accum = user_score
    for choice in unselected_choices:
        # Only consider answers from different pages or from the same page
        # and same question
        if on_same_page(choice, possible_answers):
            continue
        if better and accum <= user_score:
            possible_answers.append(choice)
            accum += choice.answer_score
        elif not better and accum >= user_score:
            possible_answers.append(choice)
            accum += choice.answer_score

    return possible_answers


def on_same_page(answer, possible_choices):
    """Check if answer is on the same page as other choices the user selected,
    excluding answers from the same question on the same page."""
    for choice in possible_choices:
        if choice.question_id != answer.question_id:
            if choice.question.page_id == answer.question.page_id:
                return True
    return False


def get_suggestions_for(questionnaire_id, user_choices, better):
    """Get suggestions for a different score, better or worse, with a minimal
    number of extra answers based on the user's choices."""

    # Get all the answers for the current questionnaire
    available_answers = answers_for_questionnaire(questionnaire_id)

    unselected_choices = []
    for answer in available_answers:
        if better:
            if answer.answer_score > 0 and answer.id not in user_choices:
                unselected_choices.append(answer)
        else:
            if answer.answer_score < 0 and answer.id not in user_choices:
                unselected_choices.append(answer)
    if better:
        unselected_choices.sort(key=lambda a: a.answer_score, reverse=True)
    else:
        unselected_choices.sort(key=lambda a: a.answer_score)

    return select_optimal_answers(user_choices, unselected_choices, better)
