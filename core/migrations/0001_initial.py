# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Branch'
        db.create_table(u'core_branch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('franchise', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('owner_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('operator_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Branch'])


    def backwards(self, orm):
        # Deleting model 'Branch'
        db.delete_table(u'core_branch')


    models = {
        u'core.branch': {
            'Meta': {'object_name': 'Branch'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'franchise': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'operator_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['core']