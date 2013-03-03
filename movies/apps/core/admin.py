# -*- coding: utf-8 -*-
from django.contrib import admin

from movies.apps.core import models


admin.site.register(models.Movie, admin.ModelAdmin)
admin.site.register(models.NewsItem, admin.ModelAdmin)
admin.site.register(models.MovieShot, admin.ModelAdmin)
admin.site.register(models.Trailer, admin.ModelAdmin)
admin.site.register(models.TopsHistory, admin.ModelAdmin)
