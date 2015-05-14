from questionnaire.models import *
import pytest


@pytest.mark.django_db(transaction=True)
def set_up(db):
    # create Questionnaire
    Questionnaire.objects.create(
        id=1,
        questionnaire_name="Questionnaire_1",
        questionnaire_description="Questionnaire 1",
        result_description="Result description",
        result_upper_limit=100
    )

    Questionnaire.objects.create(
        id=2,
        questionnaire_name="Questionnaire_2",
        questionnaire_description="Questionnaire 2",
        result_description="Result description",
        result_upper_limit=100
    )

    # create pages
    Page.objects.create(
        id=1,
        questionnaire_id=1,
        page_name="Page1_Q1",
        page_order=1
    )
    Page.objects.create(
        id=7,
        questionnaire_id=1,
        page_name="Page2_Q1",
        page_order=2
    )
    Page.objects.create(
        id=3,
        questionnaire_id=1,
        page_name="Page3_Q1",
        page_order=3
    )

    Page.objects.create(
        id=4,
        questionnaire_id=2,
        page_name="Page1_Q2",
        page_order=1
    )

    # create questions
    Question.objects.create(
        id=1,
        page_id=1,
        question_text="What's your name?",
        question_order=1
    )
    Question.objects.create(
        id=2,
        page_id=1,
        question_text="What's your age?",
        question_order=2
    )
    Question.objects.create(
        id=3,
        page_id=1,
        question_text="What's your favorite color?",
        question_order=3
    )
    Question.objects.create(
        id=6,
        page_id=3,
        question_text="What car do you drive?",
        question_order=1
    )
    Question.objects.create(
        id=7,
        page_id=3,
        question_text="What's your favorite food?",
        question_order=2
    )
    Question.objects.create(
        id=8,
        page_id=3,
        question_text="Where do you go for lunch?",
        question_order=3
    )
    Question.objects.create(
        id=9,
        page_id=7,
        question_text="What flowers do you like?",
        question_order=1
    )
    Question.objects.create(
        id=10,
        page_id=7,
        question_text="What animals do you like?",
        question_order=2
    )

    # create answers
    Answer.objects.create(
        id=2,
        answer_text="Vlad",
        answer_score=-1,
        question_id=1
    )
    Answer.objects.create(
        id=5,
        answer_text="Mercedes",
        answer_score=3,
        question_id=6
    )
    Answer.objects.create(
        id=10,
        answer_text="Lily",
        answer_score=-2,
        question_id=9
    )
    Answer.objects.create(
        id=14,
        answer_text="12",
        answer_score=2,
        question_id=2
    )
    Answer.objects.create(
        id=17,
        answer_text="Pizza",
        answer_score=8,
        question_id=7
    )
    Answer.objects.create(
        id=20,
        answer_text="Dogs",
        answer_score=1,
        question_id=10
    )
    Answer.objects.create(
        id=23,
        answer_text="Blue",
        answer_score=-1,
        question_id=3
    )
    Answer.objects.create(
        id=27,
        answer_text="Drunken Rat",
        answer_score=-3,
        question_id=8
    )
    Answer.objects.create(
        id=1,
        answer_text="Bogdan",
        answer_score=10,
        question_id=1
    )
    Answer.objects.create(
        id=3,
        answer_text="Ion",
        answer_score=2,
        question_id=1
    )
    Answer.objects.create(
        id=4,
        answer_text="BMW",
        answer_score=-4,
        question_id=6
    )
    Answer.objects.create(
        id=6,
        answer_text="Logan",
        answer_score=10,
        question_id=6
    )
    Answer.objects.create(
        id=7,
        answer_text="Lada",
        answer_score=-2,
        question_id=6
    )
    Answer.objects.create(
        id=8,
        answer_text="Roses",
        answer_score=-3,
        question_id=9
    )
    Answer.objects.create(
        id=9,
        answer_text="Anemone",
        answer_score=5,
        question_id=9
    )
    Answer.objects.create(
        id=11,
        answer_text="Aster",
        answer_score=6,
        question_id=9
    )
    Answer.objects.create(
        id=12,
        answer_text="Azalea",
        answer_score=3,
        question_id=3
    )
    Answer.objects.create(
        id=13,
        answer_text="27",
        answer_score=10,
        question_id=2
    )
    Answer.objects.create(
        id=15,
        answer_text="87",
        answer_score=-6,
        question_id=2
    )
    Answer.objects.create(
        id=16,
        answer_text="Shaorma",
        answer_score=5,
        question_id=7
    )
    Answer.objects.create(
        id=18,
        answer_text="Burger",
        answer_score=-2,
        question_id=7
    )
    Answer.objects.create(
        id=19,
        answer_text="Cats",
        answer_score=-4,
        question_id=10
    )
    Answer.objects.create(
        id=21,
        answer_text="Horses",
        answer_score=9,
        question_id=10
    )
    Answer.objects.create(
        id=22,
        answer_text="Red",
        answer_score=-3,
        question_id=3
    )
    Answer.objects.create(
        id=24,
        answer_text="Green",
        answer_score=10,
        question_id=3
    )
    Answer.objects.create(
        id=25,
        answer_text="Iulius Mall",
        answer_score=-5,
        question_id=8
    )
    Answer.objects.create(
        id=26,
        answer_text="The Note Pub",
        answer_score=8,
        question_id=8
    )


@pytest.fixture(autouse=True)
def create_db(db):
    set_up(db)


@pytest.fixture(scope="module")
def user_choices():
    return [2, 5, 10, 14, 17, 20, 23, 27]


@pytest.fixture(scope="module")
def unselected_choices():
    return [1, 3, 4, 6, 7, 8, 9, 11, 12, 13, 15, 16, 18,
            19, 21, 22, 24, 25, 26]