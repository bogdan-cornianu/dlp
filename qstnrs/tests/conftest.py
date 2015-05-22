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
    Answer.objects.bulk_create([
        Answer(answer_text="Vlad", answer_score=-1, question=name_qstn),
        Answer(answer_text="Bogdan", answer_score=10, question=name_qstn),
        Answer(answer_text="Ion", answer_score=2, question=name_qstn)
    ])
    Answer.objects.bulk_create([
        Answer(answer_text="12", answer_score=2, question=age_qstn),
        Answer(answer_text="27", answer_score=10, question=age_qstn),
        Answer(answer_text="87", answer_score=-6, question=age_qstn)
    ])
    Answer.objects.bulk_create([
        Answer(answer_text="Blue", answer_score=-1, question=colors_qstn),
        Answer(answer_text="Red", answer_score=-3, question=colors_qstn),
        Answer(answer_text="Green", answer_score=10, question=colors_qstn)
    ])
    Answer.objects.bulk_create([
        Answer(answer_text="Lily", answer_score=-2, question=flowers_qstn),
        Answer(answer_text="Roses", answer_score=-3, question=flowers_qstn),
        Answer(answer_text="Anemone", answer_score=5, question=flowers_qstn),
        Answer(answer_text="Aster", answer_score=6, question=flowers_qstn),
        Answer(answer_text="Azalea", answer_score=3, question=flowers_qstn)
    ])
    Answer.objects.bulk_create([
        Answer(answer_text="Dogs", answer_score=1, question=animals_qstn),
        Answer(answer_text="Cats", answer_score=-4, question=animals_qstn),
        Answer(answer_text="Horses", answer_score=9, question=animals_qstn)
    ])
    Answer.objects.bulk_create([
        Answer(answer_text="Mercedes", answer_score=3, question=cars_qstn),
        Answer(answer_text="BMW", answer_score=-4, question=cars_qstn),
        Answer(answer_text="Logan", answer_score=10, question=cars_qstn),
        Answer(answer_text="Lada", answer_score=-2, question=cars_qstn)
    ])
    Answer.objects.bulk_create([
        Answer(answer_text="Pizza", answer_score=8, question=food_qstn),
        Answer(answer_text="Shaorma", answer_score=5, question=food_qstn),
        Answer(answer_text="Burger", answer_score=-2, question=food_qstn)
    ])
    Answer.objects.bulk_create([
        Answer(
            answer_text="Drunken Rat", answer_score=-3, question=lunch_qstn),
        Answer(
            answer_text="Iulius Mall", answer_score=-5, question=lunch_qstn),
        Answer(
            answer_text="The Note Pub", answer_score=8, question=lunch_qstn)
    ])


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

