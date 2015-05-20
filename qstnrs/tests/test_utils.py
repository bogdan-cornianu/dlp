from questionnaire.utils import get_score_for,\
    get_suggestions_for, on_same_page, get_max_score_for
from questionnaire.models import Answer
import pytest


@pytest.mark.django_db
def test_get_score(user_choices):
    user_score = get_score_for(user_choices)
    assert user_score == 7


@pytest.mark.django_db
def test_get_suggestions_for_better(user_choices):
    suggestions = get_suggestions_for(1, user_choices, True)
    assert suggestions[0].answer_text == "27"


@pytest.mark.django_db
def test_get_suggestions_for_worse(user_choices):
    suggestions = get_suggestions_for(1, user_choices, False)
    assert suggestions[0].answer_text == "87"


@pytest.mark.django_db
def test_on_same_page(user_choices):
    user_answers = Answer.objects.filter(id__in=user_choices)
    same_page = on_same_page(Answer.objects.get(id=1), user_answers)

    assert same_page


@pytest.mark.django_db
def test_get_max_score_for():
    assert get_max_score_for(1) == 92
