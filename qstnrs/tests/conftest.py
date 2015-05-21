from questionnaire.models import Questionnaire, Answer
import pytest


@pytest.fixture(autouse=True)
def set_up(transactional_db):
    # create Questionnaire
    q1 = Questionnaire.objects.create(
        questionnaire_name="Questionnaire_1",
        questionnaire_description="Questionnaire 1"
    )

    q2 = Questionnaire.objects.create(
        questionnaire_name="Questionnaire_2",
        questionnaire_description="Questionnaire 2"
    )

    # Create pages
    p1_qstnr1 = q1.page_set.create(page_name="Page1_Q1")
    p2_qstnr1 = q1.page_set.create(page_name="Page2_Q1")
    p3_qstnr1 = q1.page_set.create(page_name="Page3_Q1")

    q2.page_set.create(page_name="Page1_Q2")

    # create questions
    name_qstn = p1_qstnr1.question_set.create(
        question_text="What's your name?")
    age_qstn = p1_qstnr1.question_set.create(question_text="What's your age?")
    colors_qstn = p1_qstnr1.question_set.create(
        question_text="What's your favorite color?")
    flowers_qstn = p2_qstnr1.question_set.create(
        question_text="What flowers do you like?")
    animals_qstn = p2_qstnr1.question_set.create(
        question_text="What animals do you like?")
    cars_qstn = p3_qstnr1.question_set.create(
        question_text="What car do you drive?")
    food_qstn = p3_qstnr1.question_set.create(
        question_text="What's your favorite food?")
    lunch_qstn = p3_qstnr1.question_set.create(
        question_text="Where do you go for lunch?")

    # create answers
    name_qstn.answer_set.create(answer_text="Vlad", answer_score=-1)
    name_qstn.answer_set.create(answer_text="Bogdan", answer_score=10)
    name_qstn.answer_set.create(answer_text="Ion", answer_score=2)
    age_qstn.answer_set.create(answer_text="12", answer_score=2)
    age_qstn.answer_set.create(answer_text="27", answer_score=10)
    age_qstn.answer_set.create(answer_text="87", answer_score=-6)
    colors_qstn.answer_set.create(answer_text="Blue", answer_score=-1)
    colors_qstn.answer_set.create(answer_text="Red", answer_score=-3)
    colors_qstn.answer_set.create(answer_text="Green", answer_score=10)
    flowers_qstn.answer_set.create(answer_text="Lily", answer_score=-2)
    flowers_qstn.answer_set.create(answer_text="Roses", answer_score=-3)
    flowers_qstn.answer_set.create(answer_text="Anemone", answer_score=5)
    flowers_qstn.answer_set.create(answer_text="Aster", answer_score=6)
    flowers_qstn.answer_set.create(answer_text="Azalea", answer_score=3)
    animals_qstn.answer_set.create(answer_text="Dogs", answer_score=1)
    animals_qstn.answer_set.create(answer_text="Cats", answer_score=-4)
    animals_qstn.answer_set.create(answer_text="Horses", answer_score=9)
    cars_qstn.answer_set.create(answer_text="Mercedes", answer_score=3)
    cars_qstn.answer_set.create(answer_text="BMW", answer_score=-4)
    cars_qstn.answer_set.create(answer_text="Logan", answer_score=10)
    cars_qstn.answer_set.create(answer_text="Lada", answer_score=-2)
    food_qstn.answer_set.create(answer_text="Pizza", answer_score=8)
    food_qstn.answer_set.create(answer_text="Shaorma", answer_score=5)
    food_qstn.answer_set.create(answer_text="Burger", answer_score=-2)
    lunch_qstn.answer_set.create(answer_text="Drunken Rat", answer_score=-3)
    lunch_qstn.answer_set.create(answer_text="Iulius Mall", answer_score=-5)
    lunch_qstn.answer_set.create(answer_text="The Note Pub", answer_score=8)


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

