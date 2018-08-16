from __future__ import unicode_literals

import errno
import os
from shutil import copyfile

from django.conf import settings
from django.core import management
from django.core.management.utils import get_random_secret_key


class Command(management.BaseCommand):
    help = 'Rollback the configuration file to the last valid version.'

    def handle(self, *args, **options):
        try:
            copyfile(
                settings.CONFIGURATION_LAST_GOOD_FILEPATH,
                settings.CONFIGURATION_FILEPATH
            )
        except IOError as exception:
            if exception.errno == errno.ENOENT:
                self.stdout.write(
                    self.style.NOTICE(
                        'There is no last valid version to restore.'
                    )
                )
            else:
                raise
