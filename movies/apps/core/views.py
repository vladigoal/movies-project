# -*- coding: utf-8 -*-
#system

#django
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

#other
from annoying.decorators import render_to

#project
from movies.apps.core import models


@render_to("core/home.html")
def home(request):
    movies_of_the_day = models.Movie.objects.all().order_by('played_times_day', 'likes_day', 'rating_score')
    movies_of_the_month = models.Movie.objects.all().order_by('played_times_month', 'likes_month', 'rating_score')
    return locals()