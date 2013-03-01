# -*- coding: utf-8 -*-
"""
Core models.
"""
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from annoying.fields import AutoOneToOneField

from .utils import unique_slug


class cls_or_inst_method(object):
    """Return different objects for class attribute access and instance attribute access
    Example:
        class Foo(object):
            def inst_bar(self):
                print('instance method')

            def cls_bar(cls):
                print('class method')

            bar = cls_or_inst_method(cls_bar, inst_bar)

    """
    def __init__(self, class_method, instance_method):
        self.class_method = class_method
        self.instance_method = instance_method

    def __get__(self, obj, parent):
        if parent is None:
            objtype = type(obj)
        else:
            objtype = parent
        if obj is None:
            print 'class'
            def newfunc(*args, **kwargs):
                return self.class_method(objtype, *args, **kwargs)
        else:
            print 'instance', parent, objtype
            def newfunc(*args, **kwargs):
                return self.instance_method(obj, *args, **kwargs)
        return newfunc


class DummyUrlMixin(object):
    TEMPLATE = "core/generic_details.html"
    LIST_TEMPLATE = "core/generic_list.html"
    DETAILS_VIEW = "movies.apps.core.views.dummy_details"
    LIST_VIEW = "movies.apps.core.views.dummy_list"

    COMMON_METHODS = ('%s_get')

    @models.permalink
    def details_get_url(self):
        """Get url for instance. You can override class or instance attribute DETAILS_VIEW to change view's path

        """
        self_type = ContentType.objects.get_for_model(self)
        app_label = self_type.app_label
        model_name = self_type.model
        return (self.DETAILS_VIEW, (),
                {"slug": self.slug, 'model_name': model_name, 'app_label': app_label})

    def details_prepare_context(self, request, *args, **kwargs):
        """Derived classes should override this method to prepare additional context dictionary for dummy_details view.

        Note that dummy_details view passes it's *args and **kwargs here
        """
        return dict()

    def details_get_template(self, request, *args, **kwargs):
        """Derived classes should set cls.TEMPLATE or instance.TEMPLATE or override this method to change template used
        by dummy_details view.
        This method should return {'TEMPLATE': 'path/to/template.thml'}

        Note that dummy_details view passes it's *args and **kwargs here
        """
        return dict(TEMPLATE=self.TEMPLATE)

    @models.permalink
    def list_get_url(cls):
        """Get url for list_view of model. You can override class attribute LIST_VIEW to change view's path

        """
        self_type = ContentType.objects.get_for_model(cls)
        app_label = self_type.app_label
        model_name = self_type.model
        return (cls.LIST_VIEW, (),
                {'model_name': model_name, 'app_label': app_label})

    def list_prepare_context(self, request, *args, **kwargs):
        """Derived classes should override this method to prepare additional context dictionary for dummy_list view.

        Note that dummy_list view passes it's *args and **kwargs here
        """
        return dict()

    def list_get_template(self, request, *args, **kwargs):
        """Derived classes should set cls.LIST_TEMPLATE or override this method to change
        template used by dummy_list view.
        This method should return {'TEMPLATE': 'path/to/template.thml'}

        Note that dummy_list view passes it's *args and **kwargs here
        """
        return dict(TEMPLATE=self.LIST_TEMPLATE)

    @classmethod
    def list_get_queryset(self, request, *args, **kwargs):
        """Derived classes should override this method to prepare additional context dictionary for dummy_list view.

        Note that dummy_list view passes it's *args and **kwargs here
        """
        return self.objects.all()

    get_url = cls_or_inst_method(list_get_url, details_get_url)
    prepare_context = cls_or_inst_method(list_prepare_context, details_prepare_context)
    get_template = cls_or_inst_method(list_get_template, details_get_template)
    get_queryset = list_get_queryset


class AutoTitleSlugMixin(object):
    def __init__(self, *args, **kwargs):
        super(AutoTitleSlugMixin, self).__init__(*args, **kwargs)
        self._prev_title = self.title

    def save(self, *args, **kwargs):
        if self._prev_title != self.title or not self.pk:
            self.slug = unique_slug(Movie, self.title)
        super(AutoTitleSlugMixin, self).save(*args, **kwargs)


class Movie(models.Model, DummyUrlMixin, AutoTitleSlugMixin):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(_("Name to be used in urls"), max_length=100, unique=True)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    played_times = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self._prev_title != self.title or not self.pk:
            self.slug = unique_slug(Movie, self.title)
        super(Movie, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("movies.apps.core.views.movie_details", (), {"slug": self.slug})


class ImagedModel(models.Model):
    image = models.ImageField(upload_to='movie-shots', height_field='image_height', width_field='image_width')
    image_width = models.SmallIntegerField(default=0)
    image_height = models.SmallIntegerField(default=0)

    class Meta:
        abstract = True


class MovieShot(ImagedModel, DummyUrlMixin):
    pass


class Trailer(ImagedModel, DummyUrlMixin):
    pass


class NewsItem(models.Model, DummyUrlMixin, AutoTitleSlugMixin):
    SHORT_TEXT_LENGTH = 150
    WORD_DELIMITERS = (u" ", u"," u".")
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(_("Name to be used in urls"), max_length=100, unique=True)
    short_text = models.CharField(max_length=100, blank=True)
    full_text = models.TextField()
    chosen_image = models.ForeignKey(MovieShot)
    chosen_trailer = models.ForeignKey(Trailer)

    def __unicode__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(NewsItem, self).__init__(*args, **kwargs)
        self._prev_full_text = self.full_text

    def save(self, *args, **kwargs):
        if self._prev_full_text != self.full_text or not self.short_text:
            self.short_text = NewsItem.get_short_text(self.full_text)
        super(NewsItem, self).save(*args, **kwargs)

    @classmethod
    def get_short_text(cls, text):
        shorter = text[:cls.SHORT_TEXT_LENGTH]
        sane_limit = int(cls.SHORT_TEXT_LENGTH / 3)
        for char in cls.WORD_DELIMITERS:
            new_limit = shorter.rfind(char)
            if new_limit >= sane_limit:
                sane_limit = new_limit
        return u"%s…" % shorter[:sane_limit]