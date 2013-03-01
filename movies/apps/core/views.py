# -*- coding: utf-8 -*-
#system

#django
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

#other
from annoying.decorators import render_to


@render_to()
def dummy_list_or_details(request, app_label, model_name, is_list=False, slug=None, *args, **kwargs):
    model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()
    if is_list:
        obj = model
        queryset = obj.get_queryset(request, *args, **kwargs)
        context = {"queryset": queryset}
    else:
        obj = model.objects.get(slug=slug)
        context = {"instance": obj}
    # please read core.models.DummyUrlMixin cocstrings for details on next two method calls
    context.update(obj.prepare_context(request, *args, **kwargs))
    context.update(obj.get_template(request, *args, **kwargs))
    print context

    return context


def dummy_list(request, app_label, model_name, *args, **kwargs):
    return dummy_list_or_details(request, app_label, model_name, is_list=True, *args, **kwargs)


def dummy_details(request, slug, app_label, model_name, *args, **kwargs):
    return dummy_list_or_details(request, app_label, model_name, slug=slug, *args, **kwargs)


@render_to("core/home.html")
def home(request):
    return {}