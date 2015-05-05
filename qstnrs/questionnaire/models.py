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
    page_order = models.IntegerField()

    def __unicode__(self):
        return self.page_name


class Question(models.Model):
    page = models.ForeignKey(Page)
    question_text = models.CharField(max_length=250)
    question_order = models.IntegerField()

    def __unicode__(self):
        return self.question_text[:100]

    class Meta:
        ordering = ['question_order']


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=50)
    answer_score = models.IntegerField()

    def __unicode__(self):
        return self.answer_text


class Result(models.Model):
    description = models.CharField(max_length=200)
    questionnaire = models.ForeignKey(Questionnaire)
    lower_limit = models.IntegerField()
    upper_limit = models.IntegerField()

    def __unicode__(self):
        return self.description
