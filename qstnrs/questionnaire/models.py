from django.db import models


class Questionnaire(models.Model):
    questionnaire_name = models.CharField(max_length=150)
    questionnaire_description = models.TextField(max_length=500)

    def __unicode__(self):
        return self.questionnaire_name[:100]

    class Meta:
        ordering = ['questionnaire_name']


class Page(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    page_name = models.CharField(max_length=50)

    class Meta:
        order_with_respect_to = 'questionnaire'

    def __unicode__(self):
        return self.page_name


class Question(models.Model):
    page = models.ForeignKey(Page)
    question_text = models.CharField(max_length=250)

    def __unicode__(self):
        return self.question_text[:100]

    class Meta:
        order_with_respect_to = 'page'


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=50)
    answer_score = models.IntegerField()

    def __unicode__(self):
        return self.answer_text
