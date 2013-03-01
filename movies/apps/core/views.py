# -*- coding: utf-8 -*-
#system

#django
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

#other
from annoying.decorators import render_to


@render_to()
def dummy_details(request, slug, app_label, model_name, *args, **kwargs):
    model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()
    instance = model.objects.get(slug=slug)
    context = {"instance": instance}

    # please read .models.DummyUrlMixin cocstrings for details on next two method calls
    context.update(instance.prepare_context(*args, **kwargs))
    context.update(instance.get_template(*args, **kwargs))

    return context


@render_to()
def dummy_list(request, app_label, model_name, *args, **kwargs):
    model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()
    queryset = model.get_list_queryset(*args, **kwargs)
    context = {"queryset": queryset}

    # please read .models.DummyUrlMixin cocstrings for details on next two method calls
    context.update(model.prepare_list_context(*args, **kwargs))
    context.update(model.get_list_template(*args, **kwargs))

    return context
