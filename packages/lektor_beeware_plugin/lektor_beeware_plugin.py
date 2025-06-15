# -*- coding: utf-8 -*-
"""This is a custom local plugin to ad extra functionality to BeeWare site."""

from datetime import date

from lektor.pluginsystem import Plugin


class BeeWarePlugin(Plugin):
    name = 'BeeWare Custom Lektor Plugin'
    description = 'This is a custom local plugin to add extra functionality.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals['today'] = date.today()
