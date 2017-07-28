#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from lektor.pluginsystem import Plugin


def is_using_fallback_alt(page):
    alt_basename = 'contents+{alt}.lr'.format(alt=page.alt)
    return (
        os.path.basename(page.source_filename) != alt_basename or
        not os.path.exists(page.source_filename)
    )


class PyBeePlugin(Plugin):
    """Plugin entry providing useful extensions for `pybee.org`.
    """
    name = 'PyBee'
    description = u'Useful extensions for pybee.org.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters.update({
            'is_using_fallback_alt': is_using_fallback_alt,
        })
