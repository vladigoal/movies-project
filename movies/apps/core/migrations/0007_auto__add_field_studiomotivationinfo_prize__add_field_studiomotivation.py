# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StudioMotivationInfo.prize'
        db.add_column('core_studiomotivationinfo', 'prize',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StudioMotivationInfo.prize_firiends_condition'
        db.add_column('core_studiomotivationinfo', 'prize_firiends_condition',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=5, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StudioMotivationInfo.prize'
        db.delete_column('core_studiomotivationinfo', 'prize')

        # Deleting field 'StudioMotivationInfo.prize_firiends_condition'
        db.delete_column('core_studiomotivationinfo', 'prize_firiends_condition')


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
            'studio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.MovieStudio']", 'null': 'True', 'blank': 'True'}),
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
        'core.moviestudio': {
            'Meta': {'object_name': 'MovieStudio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'logo_height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'logo_width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
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
        'core.studiomotivationinfo': {
            'Meta': {'object_name': 'StudioMotivationInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prize': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'prize_firiends_condition': ('django.db.models.fields.SmallIntegerField', [], {'default': '5', 'blank': 'True'}),
            'reputation_bonus': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'studio': ('annoying.fields.AutoOneToOneField', [], {'to': "orm['core.MovieStudio']", 'unique': 'True'}),
            'watch_minutes_bonus': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'})
        },
        'core.studiomotivationprogress': {
            'Meta': {'object_name': 'StudioMotivationProgress'},
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'motivationprogress_targets'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.StudioMotivationInfo']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'motivationprogress_actor'", 'to': "orm['auth.User']"})
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