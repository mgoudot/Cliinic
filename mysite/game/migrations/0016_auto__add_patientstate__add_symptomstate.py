# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PatientState'
        db.create_table('game_patientstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Patient'])),
            ('player', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('unlocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('game', ['PatientState'])

        # Adding model 'SymptomState'
        db.create_table('game_symptomstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('player', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.PatientState'])),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Symptom'])),
        ))
        db.send_create_signal('game', ['SymptomState'])


    def backwards(self, orm):
        # Deleting model 'PatientState'
        db.delete_table('game_patientstate')

        # Deleting model 'SymptomState'
        db.delete_table('game_symptomstate')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'game.case': {
            'Meta': {'object_name': 'Case'},
            'history': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Patient']"})
        },
        'game.investigate': {
            'Meta': {'object_name': 'Investigate'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Case']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Investigation']"}),
            'needed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ordered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Patient']"})
        },
        'game.investigation': {
            'Meta': {'object_name': 'Investigation'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.InvestigationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'game.investigationtodo': {
            'Meta': {'object_name': 'InvestigationToDo'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Case']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investigate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Investigate']"}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Patient']"}),
            'todo': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'game.investigationtype': {
            'Meta': {'object_name': 'InvestigationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'game.patient': {
            'Meta': {'object_name': 'Patient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'difficulty': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'game.patientstate': {
            'Meta': {'object_name': 'PatientState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Patient']"}),
            'player': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'unlocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'game.symptom': {
            'Meta': {'object_name': 'Symptom'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investigate': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['game.Investigate']", 'null': 'True', 'blank': 'True'}),
            'invrep': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'invxp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Patient']"}),
            'result': ('django.db.models.fields.CharField', [], {'default': "'negative'", 'max_length': '200'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'treat': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['game.Treat']", 'null': 'True', 'blank': 'True'}),
            'treatrep': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'treatxp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'game.symptomstate': {
            'Meta': {'object_name': 'SymptomState'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Symptom']"}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.PatientState']"}),
            'player': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'game.treat': {
            'Meta': {'object_name': 'Treat'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Case']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Treatment']"}),
            'needed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ordered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Patient']"})
        },
        'game.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'treattype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.TreatmentType']"})
        },
        'game.treatmenttype': {
            'Meta': {'object_name': 'TreatmentType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'game.userpatient': {
            'Meta': {'object_name': 'UserPatient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Patient']"}),
            'patientTreated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'game.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patientsTreated': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rep': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'xp': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['game']