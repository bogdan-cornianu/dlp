# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Questionnaire'
        db.create_table('questionnaire_questionnaire', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('questionnaire_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('questionnaire_description', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('questionnaire', ['Questionnaire'])

        # Adding model 'Page'
        db.create_table('questionnaire_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Questionnaire'])),
            ('page_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('questionnaire', ['Page'])

        # Adding model 'Answer'
        db.create_table('questionnaire_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer_text', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('questionnaire', ['Answer'])

        # Adding model 'Question'
        db.create_table('questionnaire_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Page'])),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('question_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('questionnaire', ['Question'])

        # Adding model 'QuestionAnswer'
        db.create_table('questionnaire_questionanswer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Question'])),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Answer'])),
            ('answer_score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('questionnaire', ['QuestionAnswer'])

        # Adding model 'Result'
        db.create_table('questionnaire_result', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Questionnaire'])),
            ('result_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('result_upper_limit', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('questionnaire', ['Result'])


    def backwards(self, orm):
        # Deleting model 'Questionnaire'
        db.delete_table('questionnaire_questionnaire')

        # Deleting model 'Page'
        db.delete_table('questionnaire_page')

        # Deleting model 'Answer'
        db.delete_table('questionnaire_answer')

        # Deleting model 'Question'
        db.delete_table('questionnaire_question')

        # Deleting model 'QuestionAnswer'
        db.delete_table('questionnaire_questionanswer')

        # Deleting model 'Result'
        db.delete_table('questionnaire_result')


    models = {
        'questionnaire.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer_text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'questionnaire.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Questionnaire']"})
        },
        'questionnaire.question': {
            'Meta': {'object_name': 'Question'},
            'answers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['questionnaire.Answer']", 'through': "orm['questionnaire.QuestionAnswer']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Page']"}),
            'question_order': ('django.db.models.fields.IntegerField', [], {}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'questionnaire.questionanswer': {
            'Meta': {'object_name': 'QuestionAnswer'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Answer']"}),
            'answer_score': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Question']"})
        },
        'questionnaire.questionnaire': {
            'Meta': {'object_name': 'Questionnaire'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questionnaire_description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'questionnaire_name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'questionnaire.result': {
            'Meta': {'object_name': 'Result'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Questionnaire']"}),
            'result_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'result_upper_limit': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['questionnaire']