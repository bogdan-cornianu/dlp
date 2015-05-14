from questionnaire.utils import *
import pytest


@pytest.mark.django_db
def test_get_score(user_choices):
    user_score = get_score_for(user_choices)
    assert user_score == 7


@pytest.mark.django_db
def test_answers_for_questionnaire():
    all_answers_ids = [2, 5, 10, 14, 17, 20, 23, 27, 1, 3, 4, 6, 7, 8, 9, 11,
                       12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 26]
    answers = [a.id for a in answers_for_questionnaire(1)]
    common_answers = filter(lambda answr: answr in all_answers_ids, answers)

    assert len(common_answers) == len(answers)


@pytest.mark.django_db
def test_get_suggestions_for_better(user_choices):
    suggestions = get_suggestions_for(1, user_choices, True)
    assert suggestions[0].id == 1


@pytest.mark.django_db
def test_get_suggestions_for_worse(user_choices):
    suggestions = get_suggestions_for(1, user_choices, False)
    assert suggestions[0].id == 15


@pytest.mark.django_db
def test_on_same_page(user_choices):
    user_answers = Answer.objects.filter(id__in=user_choices)
    same_page = on_same_page(Answer.objects.get(id=1), user_answers)

    assert same_page