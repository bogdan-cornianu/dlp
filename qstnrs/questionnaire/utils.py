from questionnaire.models import Answer
from django.db.models import Sum


def get_score_for(user_choices):
    """Calculate the user's total score based on selected answers."""
    return Answer.objects.filter(id__in=user_choices).aggregate(
        total=Sum('answer_score'))['total']


def get_max_score_for(questionnaire_id):
    """Get the maximum score the user could have obtained if he/she would have
     chosen only the answers with a positive score"""
    return Answer.objects.filter(
        question__page__questionnaire_id=questionnaire_id,
        answer_score__gt=0).aggregate(
        total=Sum('answer_score'))['total']


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
    available_answers = Answer.objects.filter(
        question__page__questionnaire_id=questionnaire_id)

    if better:
        unselected_qs = available_answers.filter(answer_score__gt=0).exclude(
            id__in=user_choices).order_by('-answer_score', 'answer_text')
    else:
        unselected_qs = available_answers.filter(answer_score__lt=0).exclude(
            id__in=user_choices).order_by('answer_score', 'answer_text')

    return select_optimal_answers(user_choices, unselected_qs, better)
