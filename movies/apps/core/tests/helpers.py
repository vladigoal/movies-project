# -*- coding: utf-8 -*-
import random


from django.core.files import File
from django.contrib.webdesign.lorem_ipsum import sentence, paragraph, paragraphs, words
from django.contrib.auth.models import User

import factory

from movies.apps.core import models
from movies.settings.utils import proj


def random_logo(n):
    suffix = int(n) % 4
    return File(open(proj("apps/core/tests/data/logos/logo_%s.png" % suffix)))


def random_cover(n):
    suffix = int(n) % 7
    return File(open(proj("apps/core/tests/data/covers/cover_%s.jpg" % suffix)))


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: 'user%03d' % (int(n) + 1, ))
    email = factory.LazyAttribute(lambda x: '%s@mail.com' % (x.username))

    @factory.post_generation()
    def _set_password(self, create, extracted, *args, **kwargs):
        self.set_password(self.username)
        if create:
            self.save()


class StudioFactory(factory.Factory):
    FACTORY_FOR = models.MovieStudio

    title = factory.Sequence(lambda n: 'Studio%03d %s' % (int(n) + 1, words(2)))
    logo = factory.Sequence(random_logo)

    @factory.post_generation()
    def _create_movies(self, create, extracted, *args, **kwargs):
        for i in range(random.randint(2, 4)):
            movie = MovieFactory(studio=self)
            movie.save()

    @factory.post_generation()
    def _create_motivation(self, create, extracted, *args, **kwargs):
        info = StudioMotivationInfoFactory(studio=self)
        info.save()
        progress = StudioMotivationProgressFactory(info=info)
        progress.save()


class StudioMotivationInfoFactory(factory.Factory):
    FACTORY_FOR = models.StudioMotivationInfo

    studio = factory.SubFactory(StudioFactory)
    reputation_bonus = factory.Sequence(lambda n: abs(int(n) + random.randint(-5, 23)))
    watch_minutes_bonus = factory.Sequence(lambda n: abs(int(n) + random.randint(-5, 23)))
    prize = factory.Sequence(lambda n: random.choice(('i%03dPod' % int(n), None)))
    prize_firiends_condition = factory.Sequence(lambda n: abs(int(n) + random.randint(-5, 10)))


class StudioMotivationProgressFactory(factory.Factory):
    FACTORY_FOR = models.StudioMotivationProgress

    info = factory.SubFactory(StudioMotivationInfoFactory)
    user = factory.SubFactory(UserFactory)

    @factory.post_generation(extract_prefix='friends')
    def add_friends(self, create, extracted, **kwargs):
        if extracted and type(extracted) == type(User.objects.all()):
            self.friends = extracted
            self.save()
        else:
            if User.objects.all().count() < 15:
                UserFactory.create_batch(15, **kwargs)
            for friend in User.objects.all().order_by('?')[:random.randint(1, 5)]:
                self.friends.add(friend)
            self.save()


class MovieFactory(factory.Factory):
    FACTORY_FOR = models.Movie

    title = factory.Sequence(lambda n: 'Movie%03d %s' % (int(n) + 1, words(2)))
    image = factory.Sequence(random_cover)

    short_description = factory.Sequence(lambda n: 'Movie%03d is %s' % (int(n) + 1, sentence()))
    description = factory.Sequence(lambda n: 'We can Movie%03d as %s' % (int(n) + 1, paragraph()))
    studio = factory.SubFactory(StudioFactory)

    played_times_day = factory.Sequence(lambda n: abs(int(n) + random.randint(5, 45)))
    played_times_month = factory.Sequence(lambda n: abs(int(n) + random.randint(150, 1500)))
    played_times_total = factory.Sequence(lambda n: abs(int(n) + random.randint(5000, 15000)))

    likes_day = factory.Sequence(lambda n: abs(int(n) + random.randint(0, 23)))
    likes_month = factory.Sequence(lambda n: abs(int(n) + random.randint(0, 750)))
    likes_total = factory.Sequence(lambda n: abs(int(n) + random.randint(0, 8000)))

    @factory.post_generation()
    def _create_movies(self, create, extracted, *args, **kwargs):
        for i in range(random.randint(2, 4)):
            trailer = TrailerFactory(movie=self)
            trailer.save()


class TrailerFactory(factory.Factory):
    FACTORY_FOR = models.Trailer

    image = factory.Sequence(random_cover)
    movie = factory.SubFactory(MovieFactory)


class NewsFactory(factory.Factory):
    FACTORY_FOR = models.NewsItem

    title = factory.Sequence(lambda n: 'Hot news %03d %s' % (int(n) + 1, words(2)))
    full_text = factory.Sequence(lambda n: 'Is going to be %03d %s' % (int(n) + 1, paragraphs(3
    )))

    image = factory.Sequence(random_cover)