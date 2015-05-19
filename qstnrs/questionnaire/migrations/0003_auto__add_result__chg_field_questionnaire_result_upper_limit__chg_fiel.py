# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Result'
        db.create_table('questionnaire_result', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Questionnaire'])),
            ('lower_limit', self.gf('django.db.models.fields.IntegerField')()),
            ('upper_limit', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('questionnaire', ['Result'])


        # Changing field 'Questionnaire.result_upper_limit'
        db.alter_column('questionnaire_questionnaire', 'result_upper_limit', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Questionnaire.result_description'
        db.alter_column('questionnaire_questionnaire', 'result_description', self.gf('django.db.models.fields.TextField')(max_length=500, null=True))

    def backwards(self, orm):
        # Deleting model 'Result'
        db.delete_table('questionnaire_result')


        # Changing field 'Questionnaire.result_upper_limit'
        db.alter_column('questionnaire_questionnaire', 'result_upper_limit', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Questionnaire.result_description'
        db.alter_column('questionnaire_questionnaire', 'result_description', self.gf('django.db.models.fields.TextField')(max_length=500))

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
            'result_description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True'}),
            'result_upper_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'questionnaire.result': {
            'Meta': {'object_name': 'Result'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lower_limit': ('django.db.models.fields.IntegerField', [], {}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Questionnaire']"}),
            'upper_limit': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['questionnaire']