# -*- coding: utf-8 -*-
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.template import Library
from django.utils.translation import ugettext_lazy as _

register = Library()

userpic_field = getattr(settings, 'USERPIC_FIELD', 'image')
nopic_path = getattr(settings, 'NOPIC_PATH', 'img/noavatar.png')


# TODO: create tests for this
@register.inclusion_tag('core/tags/userpic.html')
def userpic_for(user, geometry=None):
    if hasattr(user, 'userpic') or hasattr(user, 'logo'):
        profile = user
    else:
        try:
            profile = user.profile
        except:
            profile = user.get_profile()
    image = None
    url = None
    if profile:
        if hasattr(profile, 'get_userpic'):
            image = profile.get_userpic
        elif hasattr(profile, 'logo'):
            image = profile.logo
        elif hasattr(profile, 'userpic') and isinstance(profile.userpic, basestring):
            url = profile.userpic
    elif hasattr(user, 'profile'):
        havepic = (
            hasattr(profile, userpic_field) and
            getattr(profile, userpic_field)
        )
        if havepic:
            url = havepic.url
            image = havepic
        elif not hasattr(profile, userpic_field):
            raise AttributeError(_('User profile have no userpic field!'))
        else:
            url = None
            image = None
    else:
        url = staticfiles_storage.url(nopic_path)
    if geometry:
        w_h = geometry.split('x')
        width = w_h[0]
        if len(w_h) == 2:
            height = w_h[1]
        else:
            height = ''
    else:
        width = '30'
        height = '30'
    return dict(
        url=url,
        image=image,
        geometry=geometry,
        width=width,
        height=height,
    )
