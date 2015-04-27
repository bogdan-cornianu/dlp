from django.db import models


class Questionnaire(models.Model):
    questionnaire_name = models.CharField(max_length=150)
    questionnaire_description = models.CharField(max_length=400)

    def __unicode__(self):
        return self.questionnaire_name[:100]


class Page(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    page_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.page_name


class Answer(models.Model):
    answer_text = models.CharField(max_length=50)
    answer_score = models.IntegerField()

    def __unicode__(self):
        return self.answer_text


class Question(models.Model):
    page = models.ForeignKey(Page)
    answers = models.ManyToManyField(Answer)
    question_text = models.CharField(max_length=250)
    question_order = models.IntegerField()

    def __unicode__(self):
        return self.question_text[:100]


class Result(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    result_text = models.CharField(max_length=200)
    result_upper_limit = models.IntegerField()

    def __unicode__(self):
        return self.result_text[:100]
