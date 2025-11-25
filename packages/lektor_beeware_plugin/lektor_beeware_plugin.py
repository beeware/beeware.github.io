# -*- coding: utf-8 -*-
"""This is a custom local plugin to add extra functionality to the BeeWare site."""

from datetime import date

from lektor.pluginsystem import Plugin
from jinja2 import pass_context

import json


@pass_context
def languagename(context, string):
    return context["bag"](f"languages.langs.{string}")

class BeeWarePlugin(Plugin):
    name = "BeeWare Custom Lektor Plugin"
    description = "This is a custom local plugin to add extra functionality."

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals["today"] = date.today()
        self.env.jinja_env.filters["languagename"] = languagename

