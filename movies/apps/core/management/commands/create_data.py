# -*- coding: utf-8 -*-
import datetime

from django.core.management.base import NoArgsCommand
from django.utils import timezone

from movies.apps.core.tests.helpers import StudioFactory, NewsFactory
from movies.apps.core.models import TopsHistory, Movie


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        StudioFactory.create_batch(7)
        NewsFactory.create_batch(14)
        NOW = timezone.now()
        TODAY = NOW.date()
        for i in range(1, 15):
            target_date = TODAY - datetime.timedelta(i)
            movie = Movie.objects.all().order_by('?')[0]
            history = TopsHistory(rated_day=target_date, movie=movie)
            history.save()


