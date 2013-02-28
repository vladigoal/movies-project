# -*- coding: utf-8 -*-

from django.contrib.staticfiles.management.commands.runserver import Command as BaseCommand
from django.core import management


class Command(BaseCommand):

    def inner_run(self, *args, **options):
        management.call_command('collectstatic', interactive=False)
        super(Command, self).inner_run(*args, **options)

