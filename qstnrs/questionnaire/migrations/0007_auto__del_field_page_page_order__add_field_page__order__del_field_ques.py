# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Page.page_order'
        db.delete_column('questionnaire_page', 'page_order')

        # Adding field 'Page._order'
        db.add_column('questionnaire_page', '_order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Question.question_order'
        db.delete_column('questionnaire_question', 'question_order')

        # Adding field 'Question._order'
        db.add_column('questionnaire_question', '_order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Page.page_order'
        db.add_column('questionnaire_page', 'page_order',
                      self.gf('django.db.models.fields.IntegerField')(default=''),
                      keep_default=False)

        # Deleting field 'Page._order'
        db.delete_column('questionnaire_page', '_order')

        # Adding field 'Question.question_order'
        db.add_column('questionnaire_question', 'question_order',
                      self.gf('django.db.models.fields.IntegerField')(default=''),
                      keep_default=False)

        # Deleting field 'Question._order'
        db.delete_column('questionnaire_question', '_order')


    models = {
        'questionnaire.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer_score': ('django.db.models.fields.IntegerField', [], {}),
            'answer_text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Question']"})
        },
        'questionnaire.page': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Page'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Questionnaire']"})
        },
        'questionnaire.question': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Question'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Page']"}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'questionnaire.questionnaire': {
            'Meta': {'ordering': "['questionnaire_name']", 'object_name': 'Questionnaire'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questionnaire_description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'questionnaire_name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['questionnaire']