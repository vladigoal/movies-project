# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table('core_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_width', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('image_height', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, blank=True)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('played_times_day', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('played_times_month', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('played_times_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('likes_day', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('likes_month', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('likes_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('core', ['Movie'])

        # Adding model 'MovieShot'
        db.create_table('core_movieshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_width', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('image_height', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Movie'])),
        ))
        db.send_create_signal('core', ['MovieShot'])

        # Adding model 'Trailer'
        db.create_table('core_trailer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_width', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('image_height', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Movie'])),
        ))
        db.send_create_signal('core', ['Trailer'])

        # Adding model 'NewsItem'
        db.create_table('core_newsitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, blank=True)),
            ('short_text', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('full_text', self.gf('django.db.models.fields.TextField')()),
            ('chosen_image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.MovieShot'], null=True, blank=True)),
            ('chosen_trailer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Trailer'], null=True, blank=True)),
            ('creation_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('core', ['NewsItem'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table('core_movie')

        # Deleting model 'MovieShot'
        db.delete_table('core_movieshot')

        # Deleting model 'Trailer'
        db.delete_table('core_trailer')

        # Deleting model 'NewsItem'
        db.delete_table('core_newsitem')


    models = {
        'core.movie': {
            'Meta': {'object_name': 'Movie'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'likes_day': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'likes_month': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'likes_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'played_times_day': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'played_times_month': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'played_times_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'core.movieshot': {
            'Meta': {'object_name': 'MovieShot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Movie']"})
        },
        'core.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'chosen_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.MovieShot']", 'null': 'True', 'blank': 'True'}),
            'chosen_trailer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Trailer']", 'null': 'True', 'blank': 'True'}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'full_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'core.trailer': {
            'Meta': {'object_name': 'Trailer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Movie']"})
        }
    }

    complete_apps = ['core']