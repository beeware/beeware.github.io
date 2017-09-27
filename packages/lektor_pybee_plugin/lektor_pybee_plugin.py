# -*- coding: utf-8 -*-
"""This is a custom local plugin to ad extra functionality to pybee site."""
# Standrd library imports
import os
import urllib

# Third party imports
from lektor.pluginsystem import Plugin
from lektor.db import Record
from markupsafe import Markup


class PyBeePlugin(Plugin):
    name = 'PyBee Custom Lektor Plugin'
    description = 'This is a custom local plugin to ad extra functionality.'

    def on_setup_env(self, **extra):

        def is_alt_outdated(record):
            """Checks if record path (content+<alt>.lr) file exists."""
            if not isinstance(record, Record):
                raise ValueError('Must provide a `Record` object')

            config = self.env.jinja_env.globals['config']
            site = self.env.jinja_env.globals['site']
            primary_path = site.get(record.path).contents.filename
            primary_path = primary_path.replace(
                '+{0}.lr'.format(config.primary_alternative), '.lr')
            try:
                alt_path = record.contents.filename
                alt_text = '+{0}.lr'.format(config.primary_alternative)
                if alt_text in alt_path:
                    alt_path = alt_path.replace(alt_text, '.lr')
            except IOError:
                # This means the alt content file does not exist
                alt_path = None

            primary_modtime = None
            if os.path.isfile(primary_path):
                primary_modtime = os.path.getmtime(primary_path)

            alt_modtime = None
            if os.path.isfile(alt_path):
                alt_modtime = os.path.getmtime(alt_path)

            return primary_modtime > alt_modtime

        def urlencode_limit(string, limit=6000):
            """Encodes url for uri but if over limit returns None"""
            if type(string) == 'Markup':
                string = string.unescape()

            if len(string) <= limit:
                string = string.encode('utf8')
                string = urllib.quote_plus(string)
                string = Markup(string)
            else:
                string = None

            return string

        self.env.jinja_env.globals.update(is_alt_outdated=is_alt_outdated)
        self.env.jinja_env.globals.update(urlencode_limit=urlencode_limit)
        self.env.jinja_env.globals.update(dir=dir)
