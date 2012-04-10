# -*- coding: utf-8 -*-

"""

    threatmetrix.tests.__init__
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    init file for threatmetrix

"""
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'threatmetrix.tests.settings'

from .threatmetrix import *
