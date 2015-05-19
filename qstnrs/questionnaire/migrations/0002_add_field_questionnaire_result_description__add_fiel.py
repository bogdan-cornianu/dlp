# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Questionnaire.result_description'
        db.add_column('questionnaire_questionnaire', 'result_description',
                      self.gf('django.db.models.fields.TextField')(default='You did ok.', max_length=500),
                      keep_default=False)

        # Adding field 'Questionnaire.result_upper_limit'
        db.add_column('questionnaire_questionnaire', 'result_upper_limit',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Questionnaire.questionnaire_description'
        db.alter_column('questionnaire_questionnaire', 'questionnaire_description', self.gf('django.db.models.fields.TextField')(max_length=500))

    def backwards(self, orm):
        # Deleting field 'Questionnaire.result_description'
        db.delete_column('questionnaire_questionnaire', 'result_description')

        # Deleting field 'Questionnaire.result_upper_limit'
        db.delete_column('questionnaire_questionnaire', 'result_upper_limit')


        # Changing field 'Questionnaire.questionnaire_description'
        db.alter_column('questionnaire_questionnaire', 'questionnaire_description', self.gf('django.db.models.fields.CharField')(max_length=400))

    models = {
        'questionnaire.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer_score': ('django.db.models.fields.IntegerField', [], {}),
            'answer_text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Question']"})
        },
        'questionnaire.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'page_order': ('django.db.models.fields.IntegerField', [], {}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Questionnaire']"})
        },
        'questionnaire.question': {
            'Meta': {'ordering': "['question_order']", 'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Page']"}),
            'question_order': ('django.db.models.fields.IntegerField', [], {}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'questionnaire.questionnaire': {
            'Meta': {'ordering': "['questionnaire_name']", 'object_name': 'Questionnaire'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questionnaire_description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'questionnaire_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'result_description': ('django.db.models.fields.TextField', [], {'default': "'You did ok.'", 'max_length': '500'}),
            'result_upper_limit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['questionnaire']