#!/usr/bin/env python
import os
import sys
from django.conf import settings

if __name__ == "__main__":
    if os.environ.get('PROD_SERVER') == 'true':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cheukoin.settings.prod")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cheukoin.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
