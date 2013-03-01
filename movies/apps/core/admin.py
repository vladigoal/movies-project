# -*- coding: utf-8 -*-
from django.contrib import admin

from movies.apps.core.models import Movie


admin.site.register(Movie, admin.ModelAdmin)
