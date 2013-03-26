# -*- coding: utf-8 -*-
from __future__ import division
"""
Core models.
"""
#import datetime

#from django.conf import settings
#from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from djangoratings.fields import RatingField

from annoying.fields import AutoOneToOneField
from modelhelpers.mixins import DummyUrlMixin, TitleSlugifyMixin, AutoProcessFieldsMixin
from modelhelpers.utils import unique_slug


class ImagedModel(models.Model):
    image = models.ImageField(upload_to='movie-shots', height_field='image_height', width_field='image_width')
    image_width = models.SmallIntegerField(default=0, blank=True, help_text=_("Auto populated"))
    image_height = models.SmallIntegerField(default=0, blank=True, help_text=_("Auto populated"))

    class Meta:
        abstract = True


class MovieStudio(models.Model, TitleSlugifyMixin):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        _("Name to be used in urls"), max_length=100, unique=True, blank=True,
        help_text=_("Auto populated"))

    logo = models.ImageField(upload_to='studio-logos', height_field='logo_height', width_field='logo_width')
    logo_width = models.SmallIntegerField(default=0, blank=True, help_text=_("Auto populated"))
    logo_height = models.SmallIntegerField(default=0, blank=True, help_text=_("Auto populated"))


class Movie(ImagedModel, DummyUrlMixin, TitleSlugifyMixin):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        _("Name to be used in urls"), max_length=100, unique=True, blank=True,
        help_text=_("Auto populated"))

    short_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    studio = models.ForeignKey(MovieStudio, blank=True, null=True)

    played_times_day = models.IntegerField(default=0)
    played_times_month = models.IntegerField(default=0)
    played_times_total = models.IntegerField(default=0)

    likes_day = models.IntegerField(default=0)
    likes_month = models.IntegerField(default=0)
    likes_total = models.IntegerField(default=0)

    rating = RatingField(range=10)

    def __unicode__(self):
        return self.title

    def get_image_playable(self):
        if self.trailer_set.all().count():
            trailer = self.trailer_set.all()[0]
            return (trailer.image, trailer.get_url())
        if self.image:
            return (self.image, None)
        if self.movieshot_set.all().count():
            return (self.movieshot_set.all()[0].image, None)
        return None, False

    def get_image(self):
        if self.image:
            return self.image
        shots = self.movieshot_set.all()
        if shots.count():
            return shots[0].image
        return None

    def get_all_images_playable(self):
        if (self.image_width / self.image_height) > 2.05:
            wide = False
        else:
            wide = True
        images = []
        if self.image:
            images.append((self.image, False, wide))
        shots = self.movieshot_set.all()
        if shots.count():
            images.extend([(shot.image, False) for shot in shots])
        trailers = self.trailer_set.all()
        if trailers.count():
            images.extend([(trailer.image, False) for trailer in trailers])
        return images


class MovieShot(ImagedModel, DummyUrlMixin):
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return u"screenshot for movie «%s»" % self.movie.title


class Trailer(ImagedModel, DummyUrlMixin):
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return u"trailer for movie «%s»" % self.movie.title


class NewsItem(models.Model, DummyUrlMixin, AutoProcessFieldsMixin):
    SHORT_TEXT_LENGTH = 150
    WORD_DELIMITERS = (u" ", u"," u".")

    creation_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        _("Name to be used in urls"), max_length=100, unique=True, blank=True,
        help_text=_("Auto populated"))

    full_text = models.TextField()
    short_text = models.TextField(blank=True, help_text=_("Auto populated"))

    movie = models.ForeignKey(Movie, blank=True, null=True)
    chosen_image = models.ForeignKey(MovieShot, blank=True, null=True)
    chosen_trailer = models.ForeignKey(Trailer, blank=True, null=True)

    image = models.ImageField(
        upload_to='news', height_field='image_height', width_field='image_width', blank=True, null=True)
    image_width = models.SmallIntegerField(default=0, blank=True, help_text=_("Auto populated"))
    image_height = models.SmallIntegerField(default=0, blank=True, help_text=_("Auto populated"))

    def __unicode__(self):
        return self.title

    def clean(self):
        if self.movie:
            if self.chosen_image and self.chosen_image.movie != self.movie:
                raise ValidationError(_(u"Please choose image of movie «%s»") % self.movie.title)
            if self.chosen_trailer and self.chosen_trailer.movie != self.movie:
                raise ValidationError(_(u"Please choose trailer of movie «%s»") % self.movie.title)
        if not (self.movie or self.image):
            raise ValidationError(_(u"Please choose movie or image"))

    def get_image_playable(self):
        if self.image:
            return (self.image, None)
        else:
            return self.movie.get_image_playable()

    @classmethod
    def get_short_text(cls, text):
        shorter = text[:cls.SHORT_TEXT_LENGTH]
        sane_limit = int(cls.SHORT_TEXT_LENGTH / 3)
        for char in cls.WORD_DELIMITERS:
            new_limit = shorter.rfind(char)
            if new_limit >= sane_limit:
                sane_limit = new_limit
        short_text = shorter[:sane_limit]
        if short_text != text:
            short_text = u"%s…" % short_text
        return short_text

    def process_full_text(self, old_value, new_value, changed, *args, **kwargs):
        if changed or not self.pk or not self.short_text:
            self.short_text = NewsItem.get_short_text(self.full_text)

    def process_creation_time(self, old_value, new_value, changed, *args, **kwargs):
        if changed or not self.pk or not self.slug:
            if not self.creation_time:
                self.creation_time = timezone.now()
            slug_value = "%s-%s" % (self.creation_time.strftime(u"%Y-%m-%d"), self.title)
            self.slug = unique_slug(NewsItem, slug_value)

    def process_title(self, old_value, new_value, changed, old_values):
        old_creation_time = old_values['creation_time']
        if changed and old_creation_time == self.creation_time:
            # force slug recalc only when creation time is not changed
            self.process_creation_time(old_creation_time, self.creation_time,changed, old_values)


class TopsHistory(models.Model):
    movie = models.ForeignKey(Movie)
    rated_day = models.DateField(unique=True)

    class Meta:
        ordering = ['-rated_day']


class StudioMotivationInfo(models.Model):
    studio = AutoOneToOneField(MovieStudio)
    reputation_bonus = models.SmallIntegerField(default=1, blank=True)
    watch_minutes_bonus = models.SmallIntegerField(default=1, blank=True)
    prize = models.CharField(max_length=100, blank=True, null=True)
    prize_firiends_condition = models.SmallIntegerField(default=5, blank=True)


class MotivationProgressResultsWrapper(object):
    def __init__(self, counter, reputation, watch_minutes):
        self.__reputation = counter * reputation
        self.__watch_minutes = counter * watch_minutes
        self.__counter = counter

    @property
    def reputation(self):
        return self.__reputation

    @property
    def watch_minutes(self):
        return self.__watch_minutes


class StudioMotivationProgress(models.Model):
    info = models.ForeignKey(StudioMotivationInfo)
    user = models.ForeignKey(User, related_name='motivationprogress_actor')
    friends = models.ManyToManyField(User, related_name='motivationprogress_targets')

    class Meta:
        unique_together = (('info', 'user'),)

    @property
    def progress(self):
        return self.friends.all().count()

    @property
    def results(self):
        counter = self.friends.all().count()
        return MotivationProgressResultsWrapper(counter, self.info.reputation_bonus, self.info.watch_minutes_bonus)