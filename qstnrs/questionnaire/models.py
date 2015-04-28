from django.db import models


class Questionnaire(models.Model):
    questionnaire_name = models.CharField(max_length=150)
    questionnaire_description = models.CharField(max_length=400)

    def __unicode__(self):
        return self.questionnaire_name[:100]

    class Meta:
        ordering = ['questionnaire_name']


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

    class Meta:
        ordering = ['question_order']


class Result(models.Model):
    session_id = models.CharField(max_length=64)
    questionnaire = models.ForeignKey(Questionnaire)
    page = models.ForeignKey(Page)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)

    def __unicode__(self):
        return "Result " + str(self.id) + " Score:" + str(self.score)
