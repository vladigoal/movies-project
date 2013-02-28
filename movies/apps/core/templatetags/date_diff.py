from django import template
from django.utils.translation import ungettext, ugettext
from django.utils import timezone

register = template.Library()


@register.filter
def date_diff(timestamp):
    """
    Stolen from: http://djangosnippets.org/snippets/1347/

    Warning: If USE_TZ = True, timestamp must be timezone aware.
    """
    if not timestamp:
        return ""

    now = timezone.now()
    compare_with = timezone.datetime(now.year, now.month, now.day, 00, 00, 01,
                                           tzinfo=now.tzinfo)
    delta = timestamp - compare_with

    if delta.days == 0:
        return u"today"
    elif delta.days == -1:
        return u"yesterday"
    elif delta.days == 1:
        return u"tomorrow"

    chunks = (
        (365.0, lambda n: ungettext('year', 'years', n)),
        (30.0, lambda n: ungettext('month', 'months', n)),
        (7.0, lambda n: ungettext('week', 'weeks', n)),
        (1.0, lambda n: ungettext('day', 'days', n)),
    )

    for i, (chunk, name) in enumerate(chunks):
        if abs(delta.days) >= chunk:
            count = abs(round(delta.days / chunk, 0))
            break

    date_str = ugettext('%(number)d %(type)s') % {'number': count,
                                                  'type': name(count)}

    if delta.days > 0:
        return ugettext("in ") + date_str
    else:
        return date_str + ugettext(" ago")
