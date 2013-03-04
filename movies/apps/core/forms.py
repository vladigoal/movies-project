# -*- coding: utf-8 -*-
from django import forms

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import widgets

from movies.apps.core import models


class RecommendForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, label=_("Your comment"))
    photo = forms.ImageField(label=_("Attach a photo"))
    friends = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=widgets.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        self.studio = kwargs.pop('studio')
        self.user = kwargs.pop('user')
        super(RecommendForm, self).__init__(*args, **kwargs)
        self.fields['friends'].queryset = self.fields['friends'].queryset.exclude(pk=self.user.pk)
