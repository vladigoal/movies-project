# -*- coding: utf-8 -*-
from functools import wraps

from django.contrib.sites.models import Site
from django.db.models.signals import post_save
#from django.template.defaultfilters import slugify
from django.utils.functional import Promise
from django.utils.simplejson import JSONEncoder
from django.utils.encoding import force_unicode
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

from pytils.translit import slugify
from sorl.thumbnail import get_thumbnail


def get_full_url(request, path):
    full_url = request.build_absolute_uri(path)
    if settings.IS_TESTING:
        full_url = full_url.replace('testserver', Site.objects.get_current().domain)
    return full_url


def unique_slug(model, slug_value, slug_field='slug'):
    #http://djangosnippets.org/snippets/728/
    orig_slug = slug = slugify(slug_value)

    index = 0

    while True:
        try:
            model.objects.get(**{slug_field: slug})
            index += 1
            slug = orig_slug + '-' + str(index)
        except model.DoesNotExist:
            return slug


class LazyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return super(LazyEncoder, self).default(obj)

encoder = LazyEncoder()

dumps = encoder.encode