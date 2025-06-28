# -*- coding: utf-8 -*-
"""This is a custom local plugin to add extra functionality to the BeeWare site."""

from datetime import date

from lektor.pluginsystem import Plugin
from jinja2 import pass_context


@pass_context
def translate(context, string, bag_name="translate"):
    if bag_name == 'translate':
        raise RuntimeError("Use the new gettext system instead")

    # Make sure that any macros which need to call this are imported with context.
    alt = context["this"].alt
    bag = context["bag"]
    if trans := bag(f"{bag_name}.{alt}.{string}"):
        return trans

    if en := bag(f"{bag_name}.en.{string}"):
        return en

    return ""


class BeeWarePlugin(Plugin):
    name = "BeeWare Custom Lektor Plugin"
    description = "This is a custom local plugin to add extra functionality."

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals["today"] = date.today()
        self.env.jinja_env.filters["trans"] = translate
