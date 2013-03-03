# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewsItem.image'
        db.add_column('core_newsitem', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'NewsItem.image_width'
        db.add_column('core_newsitem', 'image_width',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'NewsItem.image_height'
        db.add_column('core_newsitem', 'image_height',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewsItem.image'
        db.delete_column('core_newsitem', 'image')

        # Deleting field 'NewsItem.image_width'
        db.delete_column('core_newsitem', 'image_width')

        # Deleting field 'NewsItem.image_height'
        db.delete_column('core_newsitem', 'image_height')


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Movie']", 'null': 'True', 'blank': 'True'}),
            'short_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'core.topshistory': {
            'Meta': {'ordering': "['-rated_day']", 'object_name': 'TopsHistory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Movie']"}),
            'rated_day': ('django.db.models.fields.DateField', [], {'unique': 'True'})
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