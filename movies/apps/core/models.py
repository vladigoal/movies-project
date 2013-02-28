# -*- coding: utf-8 -*-
"""
Core models.
"""
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from annoying.fields import AutoOneToOneField