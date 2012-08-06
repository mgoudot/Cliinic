# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('game_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('rep', self.gf('django.db.models.fields.IntegerField')()),
            ('xp', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('patientsTreated', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('game', ['UserProfile'])

        # Adding model 'Patient'
        db.create_table('game_patient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('difficulty', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('game', ['Patient'])

        # Adding model 'UserPatient'
        db.create_table('game_userpatient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Patient'])),
            ('patientTreated', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('game', ['UserPatient'])

        # Adding model 'Case'
        db.create_table('game_case', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Patient'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('history', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('game', ['Case'])

        # Adding model 'InvestigationType'
        db.create_table('game_investigationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('game', ['InvestigationType'])

        # Adding model 'Investigation'
        db.create_table('game_investigation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.InvestigationType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('game', ['Investigation'])

        # Adding model 'Investigate'
        db.create_table('game_investigate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Case'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Patient'])),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Investigation'])),
            ('ordered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('game', ['Investigate'])

        # Adding model 'Symptom'
        db.create_table('game_symptom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('game', ['Symptom'])

        # Adding model 'InvestigationToDo'
        db.create_table('game_investigationtodo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('investigate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Investigate'])),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Case'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Patient'])),
            ('todo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('game', ['InvestigationToDo'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('game_userprofile')

        # Deleting model 'Patient'
        db.delete_table('game_patient')

        # Deleting model 'UserPatient'
        db.delete_table('game_userpatient')

        # Deleting model 'Case'
        db.delete_table('game_case')

        # Deleting model 'InvestigationType'
        db.delete_table('game_investigationtype')

        # Deleting model 'Investigation'
        db.delete_table('game_investigation')

        # Deleting model 'Investigate'
        db.delete_table('game_investigate')

        # Deleting model 'Symptom'
        db.delete_table('game_symptom')

        # Deleting model 'InvestigationToDo'
        db.delete_table('game_investigationtodo')


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
        'game.symptom': {
            'Meta': {'object_name': 'Symptom'},
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