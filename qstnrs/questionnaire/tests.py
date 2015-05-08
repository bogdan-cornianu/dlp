from django.test import TestCase
from questionnaire.utils import *
from questionnaire.models import *


class UtilsTest(TestCase):
    fixtures = ['db.json']

    def setUp(self):
        self.user_choices = [2, 5, 10, 14, 17, 20, 23, 27]
        self.unselected_choices = [1, 3, 4, 6, 7, 8, 9, 11, 12, 13, 15, 16, 18,
                                   19, 21, 22, 24, 25, 26]

    def test_get_score(self):
        score = get_score_for(self.user_choices)
        self.assertEqual(score, 7)

    def test_get_categories_for_score(self):
        categories = get_categories_for_score(7, 1)
        # for the first questionnaire with a score of 7, all categories should
        # be included
        expected_categories = Result.objects.filter(questionnaire_id=1)
        self.assertEqual([cat.id for cat in categories],
                         [exp_cat.id for exp_cat in expected_categories])

    def test_get_minimal_better(self):
        # get minimal better for questionnaire with id = 1
        minimal_better = get_minimal_better(1, self.user_choices)
        expected = {"What's your name?": ['Ion'],
                    'What flowers do you like?': ['Azalea']}
        self.assertEqual(minimal_better, expected)

    def test_get_minimal_worse(self):
        # get minimal worse for questionnaire with id = 1
        minimal_worse = get_minimal_worse(1, self.user_choices)
        expected = {'Where do you go for lunch?': ['Iulius Mall'],
                    "What's your age?": ['87'],
                    'What animals do you like?': ['Cats']}

        self.assertEqual(minimal_worse, expected)

    def test_select_optimal_answers(self):
        unselected = [answer for answer in Answer.objects.all()
                      if answer.id in self.unselected_choices]

        optimal_answers_better = select_optimal_answers(1, self.user_choices,
                                                        unselected,
                                                        better=True)
        optimal_answers_worse = select_optimal_answers(1, self.user_choices,
                                                       unselected,
                                                       better=False)

        expected_optimal_better = {"What's your name?": ['Bogdan']}
        expected_optimal_worse = {"What's your name?": ['Bogdan', 'Ion']}

        self.assertEqual(optimal_answers_better, expected_optimal_better)
        self.assertEqual(optimal_answers_worse, expected_optimal_worse)

    def test_get_closest_limit(self):
        categories = Result.objects.filter(questionnaire_id=1)
        closest_limit_better = get_closest_limit(categories, 7, better=True)
        closest_limit_worse = get_closest_limit(categories, 7, better=False)

        self.assertEqual(closest_limit_better, 10)
        self.assertEqual(closest_limit_worse, -5)

    def test_on_same_page(self):
        answer_bogdan = Answer.objects.get(id=1)
        answers_on_same_page = Answer.objects.filter(id__in=[22, 23, 24, 13,
                                                     14, 15])
        answers_not_same_page = Answer.objects.filter(id__in=[4, 5, 6, 7,
                                                     8, 9])
        answers_same_page_same_question = Answer.objects.filter(id__in=[2, 3])

        result_same_page = on_same_page(answer_bogdan, answers_on_same_page)
        result_not_same_page = on_same_page(answer_bogdan,
                                            answers_not_same_page)
        result_same_page_same_question = on_same_page(answer_bogdan,
                                               answers_same_page_same_question)

        self.assertEqual(result_same_page, True)
        self.assertEqual(result_not_same_page, False)
        self.assertEqual(result_same_page_same_question, False)
