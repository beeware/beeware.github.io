# -*- coding: utf-8 -*-
"""This is a custom local plugin to ad extra functionality to pybee site."""
# Standrd library imports
import urllib

# Third party imports
from lektor.pluginsystem import Plugin
from lektor.db import Record
from markupsafe import Markup


class PyBeePlugin(Plugin):
    name = 'PyBee Custom Lektor Plugin'
    description = 'This is a custom local plugin to ad extra functionality.'

    def on_setup_env(self, **extra):

        def is_alt_content_available(record):
            """Checks if record path (content+<alt>.lr) file exists."""
            if not isinstance(record, Record):
                raise ValueError('Must provide a `Record` object')

            alt_available = True
            config = self.env.jinja_env.globals['config']
            if record.alt != config.primary_alternative:
                try:
                    record.contents.as_text()
                except IOError:
                    # This means the alt content file does not exist
                    alt_available = False

            return alt_available

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

        self.env.jinja_env.globals.update(
            is_alt_content_available=is_alt_content_available
        )
        self.env.jinja_env.globals.update(urlencode_limit=urlencode_limit)
