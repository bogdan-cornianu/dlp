from questionnaire.models import Questionnaire, Page, Question, Answer
import pytest


@pytest.fixture(autouse=True)
def set_up(transactional_db):
    # create Questionnaire
    Questionnaire.objects.create(
        questionnaire_name="Questionnaire_1",
        questionnaire_description="Questionnaire 1"
    )

    Questionnaire.objects.create(
        questionnaire_name="Questionnaire_2",
        questionnaire_description="Questionnaire 2"
    )

    # create pages
    Page.objects.create(
        questionnaire_id=1,
        page_name="Page1_Q1",
        page_order=1
    )
    Page.objects.create(
        questionnaire_id=1,
        page_name="Page2_Q1",
        page_order=2
    )
    Page.objects.create(
        questionnaire_id=1,
        page_name="Page3_Q1",
        page_order=3
    )

    Page.objects.create(
        questionnaire_id=2,
        page_name="Page1_Q2",
        page_order=1
    )

    # create questions
    Question.objects.create(
        page_id=1,
        question_text="What's your name?",
        question_order=1
    )
    Question.objects.create(
        page_id=1,
        question_text="What's your age?",
        question_order=2
    )
    Question.objects.create(
        page_id=1,
        question_text="What's your favorite color?",
        question_order=3
    )
    Question.objects.create(
        page_id=3,
        question_text="What car do you drive?",
        question_order=1
    )
    Question.objects.create(
        page_id=3,
        question_text="What's your favorite food?",
        question_order=2
    )
    Question.objects.create(
        page_id=3,
        question_text="Where do you go for lunch?",
        question_order=3
    )
    Question.objects.create(
        page_id=2,
        question_text="What flowers do you like?",
        question_order=1
    )
    Question.objects.create(
        page_id=2,
        question_text="What animals do you like?",
        question_order=2
    )

    # create answers
    Answer.objects.create(
        answer_text="Vlad",
        answer_score=-1,
        question_id=1
    )
    Answer.objects.create(
        answer_text="Mercedes",
        answer_score=3,
        question_id=4
    )
    Answer.objects.create(
        answer_text="Lily",
        answer_score=-2,
        question_id=7
    )
    Answer.objects.create(
        answer_text="12",
        answer_score=2,
        question_id=2
    )
    Answer.objects.create(
        answer_text="Pizza",
        answer_score=8,
        question_id=5
    )
    Answer.objects.create(
        answer_text="Dogs",
        answer_score=1,
        question_id=8
    )
    Answer.objects.create(
        answer_text="Blue",
        answer_score=-1,
        question_id=3
    )
    Answer.objects.create(
        answer_text="Drunken Rat",
        answer_score=-3,
        question_id=6
    )
    Answer.objects.create(
        answer_text="Bogdan",
        answer_score=10,
        question_id=1
    )
    Answer.objects.create(
        answer_text="Ion",
        answer_score=2,
        question_id=1
    )
    Answer.objects.create(
        answer_text="BMW",
        answer_score=-4,
        question_id=4
    )
    Answer.objects.create(
        answer_text="Logan",
        answer_score=10,
        question_id=4
    )
    Answer.objects.create(
        answer_text="Lada",
        answer_score=-2,
        question_id=4
    )
    Answer.objects.create(
        answer_text="Roses",
        answer_score=-3,
        question_id=7
    )
    Answer.objects.create(
        answer_text="Anemone",
        answer_score=5,
        question_id=7
    )
    Answer.objects.create(
        answer_text="Aster",
        answer_score=6,
        question_id=7
    )
    Answer.objects.create(
        answer_text="Azalea",
        answer_score=3,
        question_id=7
    )
    Answer.objects.create(
        answer_text="27",
        answer_score=10,
        question_id=2
    )
    Answer.objects.create(
        answer_text="87",
        answer_score=-6,
        question_id=2
    )
    Answer.objects.create(
        answer_text="Shaorma",
        answer_score=5,
        question_id=5
    )
    Answer.objects.create(
        answer_text="Burger",
        answer_score=-2,
        question_id=5
    )
    Answer.objects.create(
        answer_text="Cats",
        answer_score=-4,
        question_id=8
    )
    Answer.objects.create(
        answer_text="Horses",
        answer_score=9,
        question_id=8
    )
    Answer.objects.create(
        answer_text="Red",
        answer_score=-3,
        question_id=3
    )
    Answer.objects.create(
        answer_text="Green",
        answer_score=10,
        question_id=3
    )
    Answer.objects.create(
        answer_text="Iulius Mall",
        answer_score=-5,
        question_id=6
    )
    Answer.objects.create(
        answer_text="The Note Pub",
        answer_score=8,
        question_id=6
    )


@pytest.fixture
def user_choices():
    return Answer.objects.filter(
        answer_text__in=['Vlad', '12', 'Blue', 'Lily', 'Dogs', 'Mercedes',
                         'Pizza', 'Drunken Rat']).values_list('id', flat=True)


@pytest.fixture
def unselected_choices():
    """Get unselected choices for the first questionnaire"""
    return Answer.objects.filter(question__page__questionnaire_id=1).exclude(
        answer_text__in=['Vlad', '12', 'Blue', 'Lily', 'Dogs', 'Mercedes',
                         'Pizza', 'Drunken Rat']).values_list('id', flat=True)